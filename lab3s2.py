import os
import random
import shutil
import csv

# Функция для копирования датасета с измененными именами файлов
def copy_dataset_with_new_names(source_dir, destination_dir):
    os.makedirs(destination_dir, exist_ok=True)
    annotation_data = []
    classes = os.listdir(source_dir)

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