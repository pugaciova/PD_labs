import os
import shutil
import csv

# Функция для копирования датасета с измененными именами файлов
def copy_dataset_with_new_names(classes, source_dir, destination_dir):
    os.makedirs(destination_dir, exist_ok=True)
    annotation_data = []

    for class_name in classes:
        source_class_dir = os.path.join(source_dir, class_name)
        destination_class_dir = os.path.join(destination_dir, class_name)

        os.makedirs(destination_class_dir, exist_ok=True)

        for i, filename in enumerate(os.listdir(source_class_dir)):
            if filename.endswith('.jpg'):
                new_filename = f'{class_name}_{str(i).zfill(4)}.jpg'
                source_file_path = os.path.join(source_class_dir, filename)
                destination_file_path = os.path.join(destination_class_dir, new_filename)
                shutil.copyfile(source_file_path, destination_file_path)
                annotation_data.append([os.path.abspath(destination_file_path), os.path.relpath(destination_file_path, start=destination_dir), class_name])

    return annotation_data

# Функция для создания CSV-файла аннотации
def create_annotation_file(annotation_data, annotation_file_name):
    with open(annotation_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Absolute Path', 'Relative Path', 'Class'])
        writer.writerows(annotation_data)

if __name__ == '__main__':
    source_dataset_dir = 'dataset'  # Исходная директория датасета
    destination_dataset_dir = 'new_dataset'  # Новая директория с измененными именами файлов

    classes = ['zebra', 'bay-horse']

    annotation_data = copy_dataset_with_new_names(classes, source_dataset_dir, destination_dataset_dir)
    create_annotation_file(annotation_data, 'new_annotation.csv')

    print(f"Датасет скопирован в '{destination_dataset_dir}' с измененными именами файлов.")
    print("Файл аннотации создан: new_annotation.csv")
