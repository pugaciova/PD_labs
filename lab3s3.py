import os
import random
import shutil

# Функция для создания копии датасета с измененными именами файлов
def create_randomized_dataset(source_dir, destination_dir):
    os.makedirs(destination_dir, exist_ok=True)

    for class_name in os.listdir(source_dir):
        source_class_dir = os.path.join(source_dir, class_name)

        if not os.path.isdir(source_class_dir):
            continue

        for filename in os.listdir(source_class_dir):
            if filename.endswith('.jpg'):
                random_number = random.randint(0, 10000)
                new_filename = f'{str(random_number).zfill(4)}.jpg'
                source_file_path = os.path.join(source_class_dir, filename)
                destination_file_path = os.path.join(destination_dir, new_filename)
                shutil.copyfile(source_file_path, destination_file_path)

if __name__ == '__main__':
    source_dataset_dir = 'dataset'  # Исходная директория датасета
    randomized_dataset_dir = 'randomized_dataset'  # Директория для случайного датасета

    create_randomized_dataset(source_dataset_dir, randomized_dataset_dir)

    print(f"Случайный датасет создан в '{randomized_dataset_dir}'.")
