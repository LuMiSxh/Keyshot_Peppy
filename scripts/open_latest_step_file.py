import glob
import os

# CONST
# Pfad zum Ordner (Statisch von der Skript-Datei aus) BSP: "/path/to/folder"
path_to_folder: str = ""


def open_latest_step_file() -> None:
    # check for empty CONST
    if not path_to_folder:
        raise ValueError("Missing CONST: 'path_to_folder'")

    # computation
    files: list[str] = glob.glob(f'{path_to_folder}/*')
    latest_file: str = max(files, key=os.path.getctime)

    # check for empty latest_file
    if not latest_file:
        raise ValueError("Not files were found in the given directory")

    lux.importFile(latest_file)


if __name__ == '__main__':
    open_latest_step_file()
