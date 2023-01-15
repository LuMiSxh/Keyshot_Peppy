# NEZUMI:IGNORE_LINT
import glob
import os

# CONST
# Pfad zum Ordner (Statisch von der Skript-Datei aus) BSP: "/path/to/folder"
path_to_folder: str = ""


def open_latest() -> None:
    # check for empty CONST
    if not path_to_folder:
        raise ValueError("Missing CONST: 'path_to_folder'")

    # computation
    files = glob.glob(f'{path_to_folder}/*')
    latest_file = max(files, key=os.path.getctime)
    lux.importFile(latest_file)


# NEZUMI:ENTRYPOINT
if __name__ == '__main__':
    open_latest()
