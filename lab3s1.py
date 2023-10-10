import os
import csv

# Функция для создания CSV-файла аннотации
def create_annotation_file(classes):
    with open('annotation.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Absolute Path', 'Relative Path', 'Class'])

        for class_name in classes:
            folder_name = f'dataset/{class_name}'
            for filename in os.listdir(folder_name):
                if filename.endswith('.jpg'):
                    absolute_path = os.path.join(os.getcwd(), folder_name, filename)
                    relative_path = os.path.join('dataset', class_name, filename)
                    writer.writerow([absolute_path, relative_path, class_name])

if __name__ == '__main__':
    classes = ['zebra', 'bay-horse']

    create_annotation_file(classes)

    print("Файл аннотации создан: annotation.csv")
