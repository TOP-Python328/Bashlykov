from pathlib import Path
    
def list_files(absolute_path: str) -> tuple | None:
    
    """Возвращает кортеж с именами файлов в каталоге по переданному пути или None."""

    path = Path(absolute_path)
    
    if path.is_dir():
        file_names = tuple(file.name for file in path.iterdir() if file.is_file())
        
        return file_names
        
    return print("None")
    
# C:\Users\Asus\OneDrive\Рабочий стол\Program\dz_python\Bashlykov\2023.07.02
 # 22:10:45 > python -i 1.py
# >>> list_files(r'C:\Users\Asus\OneDrive\Рабочий стол\Program\dz_python\Bashlykov\2023.07.02\data')
# ('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')

# C:\Users\Asus\OneDrive\Рабочий стол\Program\dz_python\Bashlykov\2023.07.02
 # 22:19:19 > python -i 1.py
# >>> list_files(r'C:\Users\Asus\OneDrive\Рабочий стол\Program\dz_python\Bashlykov\2023.07.02\HW 2023.07.02')
# None