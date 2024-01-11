from dataclasses import dataclass
from os import name as os_name
from typing import Self
from sys import path


if os_name == 'nt':
    PATH_SEP = '\\'
else:
    PATH_SEP = '/'


@dataclass
class File:
    """Файл в файловой системе."""
    name: str
    dir: str
    
    @property
    def extension(self) -> str:
        return ''.join(self.name.rsplit('.', 1)[1:])
    
    def ls(self) -> str:
        return self.dir_path + PATH_SEP + self.name


class Folder(list):
    """Каталог в файловой системе. Может содержать вложенные каталоги и файлы."""
    
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.dir_path = path[0]
  
    def ls(self) -> str:
        return self.dir_path + PATH_SEP + self.name
 
    def add_nested(self, other: Self | File) -> None:
        """Добавить(переместить) в каталог элемент (файл либо каталог)"""
        if hasattr(other, 'folder'):
            other.folder.remove(other)
        other.dir_path = self.ls()
        other.folder = self
        self.append(other)


def ls(*objects: File | Folder) -> str:
    for obj in objects:
        print(obj.ls(), obj.name, obj.dir_path)


# C:\Users\Asus\Desktop\Program\dz_python\Bashlykov\2023.11.24
 # 22:08:41 > python -i 4.py
# >>> file1 = File('file1', path[0])
# >>> file2 = File('file2', path[0])
# >>> file3 = File('file3', path[0])
# >>> file4 = File('file4', path[0])
# >>>
# >>> folder1 = Folder('folder1')
# >>> folder2 = Folder('folder2')
# >>>
# >>> folder1.add_nested(file1)
# >>> folder1.add_nested(file2)
# >>>
# >>> folder2.add_nested(file3)
# >>> folder2.add_nested(file4)
# >>>
# >>> for item in folder1:
# ...     print(item.name)
# ...
# file1
# file2
# >>> for item in folder2:
# ...     print(item.name)
# ...
# file3
# file4
# >>> 
# >>> folder1.add_nested(folder2)
# >>> for item in folder1:
# ...     print(item.name)
# ...
# file1
# file2
# folder2
# >>>
# >>> objects = [file1, file2, file3, file4, folder1, folder2]
# >>>
# >>> ls(*objects)
# C:\Users\Asus\Desktop\Program\dz_python\Bashlykov\2023.11.24\folder1\file1 file1 C:\Users\Asus\Desktop\Program\dz_python\Bashlykov\2023.11.24\folder1
# C:\Users\Asus\Desktop\Program\dz_python\Bashlykov\2023.11.24\folder1\file2 file2 C:\Users\Asus\Desktop\Program\dz_python\Bashlykov\2023.11.24\folder1
# C:\Users\Asus\Desktop\Program\dz_python\Bashlykov\2023.11.24\folder2\file3 file3 C:\Users\Asus\Desktop\Program\dz_python\Bashlykov\2023.11.24\folder2
# C:\Users\Asus\Desktop\Program\dz_python\Bashlykov\2023.11.24\folder2\file4 file4 C:\Users\Asus\Desktop\Program\dz_python\Bashlykov\2023.11.24\folder2
# C:\Users\Asus\Desktop\Program\dz_python\Bashlykov\2023.11.24\folder1 folder1 C:\Users\Asus\Desktop\Program\dz_python\Bashlykov\2023.11.24
# C:\Users\Asus\Desktop\Program\dz_python\Bashlykov\2023.11.24\folder1\folder2 folder2  C:\Users\Asus\Desktop\Program\dz_python\Bashlykov\2023.11.24\folder1
# >>>