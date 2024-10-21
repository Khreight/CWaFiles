import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CompileCFilesHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.modified_files = set()
        self.last_errors = set()
        self.last_modified_time = {}

    def on_modified(self, event):
        if event.src_path.endswith('.c') and event.event_type != 'created':
            current_time = time.time()
            if event.src_path in self.last_modified_time:
                if current_time - self.last_modified_time[event.src_path] < 1.0:
                    return

            self.last_modified_time[event.src_path] = current_time


            if os.path.getsize(event.src_path) > 0:
                print(f"\n   [+] Modification détectée sur le fichier : {event.src_path}")
                time.sleep(0.5)
                self.compile_file(event.src_path)
            else:
                print(f"   [-] Ignorer le fichier vide : {event.src_path}")

    def compile_file(self, file_path):
        directory = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        executable_name = os.path.splitext(file_name)[0] + '.exe'
        obj_name = os.path.splitext(file_name)[0] + '.obj'
        
        compile_command = f'cl "{file_path}" /Fe"{os.path.join(directory, executable_name)}" /Fo"{os.path.join(directory, obj_name)}"'
        
        process = subprocess.Popen(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print(f"   |\n   └─> Compilation réussie : {executable_name} créé.")
        else:
            print("   |\n   └─> Erreur de compilation :")
            self.display_errors(stdout.decode('cp1252', errors='replace'))

    def display_errors(self, error_output):
        error_lines = error_output.splitlines()

        if error_lines:
            for line in error_lines:
                line = self.replace_special_characters(line)

                if line not in self.last_errors:
                    self.last_errors.add(line)
                    print(f"       └-> {line}")
        else:
            # Si aucune ligne d'erreur n'est trouvée
            print("       └-> [!] Aucun message d'erreur pertinent trouvé.")

    def replace_special_characters(self, text):
        replacements = {
            'é': 'e',
            'è': 'e',
            'ê': 'e',
            'ë': 'e',
            'â': 'a',
            'î': 'i',
            'ô': 'o',
            'û': 'u',
            'ç': 'c',
            'ÿ': 'y',
            '…': '...',
            '‘': "'",
            '’': "'",
            '“': '"',
            '”': '"',
            '–': '-',
            '—': '-',
            '°': '',
            '¼': '1/4',
            '½': '1/2',
            '¾': '3/4'
        }
        for special, normal in replacements.items():
            text = text.replace(special, normal)
        return text


def monitor_directory(directory_path):
    event_handler = CompileCFilesHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory_path, recursive=False)
    observer.start()
    print(f"Surveillance du dossier : {directory_path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    directory_to_watch = input("Entrez le chemin du dossier à surveiller : ")
    monitor_directory(directory_to_watch)
