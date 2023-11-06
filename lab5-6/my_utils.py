import os
from datetime import datetime
from PIL import Image
import subprocess

def get_current_date():
    """
    Получает текущую дату и время.

    Returns:
        str: Строка с текущей датой и временем в формате 'ГГГГ-ММ-ДД ЧЧ:ММ:СС'.
    """
    current_date = datetime.now()
    return current_date.strftime('%Y-%m-%d %H:%M:%S')

def list_files_in_directory(directory_path):
    """
    Возвращает список файлов в указанной директории.

    Args:
        directory_path (str): Путь к директории, в которой нужно получить список файлов.

    Returns:
        list: Список файлов в указанной директории.
    """
    if os.path.isdir(directory_path):
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return files
    else:
        return []
def display_image(image_path):
    """
    Открывает изображение из указанного пути в отдельном окне.

    Args:
        image_path (str): Путь к изображению.

    Returns:
        None
    """
    try:
        image = Image.open(image_path)
        image.show()
    except Exception as e:
        print(f"Ошибка при открытии изображения: {e}")