# import os
# import csv

# # Функция для создания CSV-файла аннотации
# def create_annotation_file(dataset_dir, annotation_file_path):
#     with open(annotation_file_path, 'w', newline='') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(['Absolute Path', 'Relative Path', 'Class'])

#         for class_name in os.listdir(dataset_dir):
#             folder_name = os.path.join(dataset_dir, class_name)
#             if os.path.isdir(folder_name):
#                 for filename in os.listdir(folder_name):
#                     if filename.endswith('.jpg'):
#                         absolute_path = os.path.join(os.getcwd(), folder_name, filename)
#                         relative_path = os.path.join('dataset', class_name, filename)
#                         writer.writerow([absolute_path, relative_path, class_name])

# if __name__ == '__main__':
#     classes = ['zebra', 'bay-horse']
#     dataset_dir = 'dataset'  # Замените на путь к вашей директории датасета
#     annotation_file_path = 'annotation.csv'  # Замените на путь, по которому вы хотите сохранить аннотацию

#     create_annotation_file(dataset_dir, annotation_file_path)

#     print("Файл аннотации создан: annotation.csv")
import os
import csv

# Функция для создания CSV-файла аннотации
def create_annotation_file(annotation_data, annotation_file_name):
    with open(annotation_file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Absolute Path', 'Relative Path', 'Class'])
        writer.writerows(annotation_data)

