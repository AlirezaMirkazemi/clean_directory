import json
from pathlib import Path
from shutil import move
from typing import Union
from loguru import logger

from src.data import DATA_DIR

with open(DATA_DIR / 'extensions.json') as f:
    file_extensions = json.load(f)


class OrganizeFiles():
    def __init__(self, extensions=file_extensions):
        extensions = {}
        for file_, ext in file_extensions.items():
            for ind in range(len(ext)):
                extensions[ext[ind]] = file_
        self.extensions = extensions

    def __call__(self, file_path: Union[Path, str]):
        
        file_path = Path(file_path)
        for file_ in file_path.iterdir():
            if file_.is_dir() == True:
                continue
            if file_.suffix in self.extensions.keys():
                folder_name = self.extensions[file_.suffix.lower()]
            else:
                folder_name = 'Others'
            
            dest_path = file_path / folder_name
            dest_path.mkdir(exist_ok=True)
            logger.info(f'moving {str(file_):10} to =====> {str(dest_path):80}')
            move(str(file_path/file_), str(dest_path))

if __name__ == '__main__':
    moving = OrganizeFiles()
    moving('/mnt/e')