import os
import random

# Функция для получения следующего экземпляра класса
def get_next_instance(class_name, dataset_dir):
    class_dir = os.path.join(dataset_dir, class_name)
    
    if not os.path.exists(class_dir) or not os.path.isdir(class_dir):
        return None

    # Получить список файлов для класса
    files = [f for f in os.listdir(class_dir) if f.endswith('.jpg')]

    if not files:
        return None

    # Перемешать список файлов случайным образом
    random.shuffle(files)

    # Пройти по файлам в случайном порядке и возвращать следующий файл
    for filename in files:
        file_path = os.path.join(class_dir, filename)
        yield file_path

# Пример использования функции
if __name__ == '__main__':
    dataset_dir = 'dataset'  # Директория с датасетом
    class_name = 'zebra'  # Метка класса, для которой нужно получать экземпляры

    instance_generator = get_next_instance(class_name, dataset_dir)

    while True:
        next_instance = next(instance_generator, None)
        if next_instance is None:
            print(f"Все экземпляры класса '{class_name}' закончились.")
            break
        else:
            print(f"Следующий экземпляр класса '{class_name}': {next_instance}")
