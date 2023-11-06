import my_utils

current_date = my_utils.get_current_date()
print(f"Текущая дата и время: {current_date}")

directory_path = "C:\\pd_labs\\dataset\\zebra"
files = my_utils.list_files_in_directory(directory_path)
print(f"Файлы в директории {directory_path}: {files}")

image_path = input('Enter image path:')
#image_path = "C:\\pd_labs\\dataset\\zebra\\0000.jpg"
my_utils.display_image(image_path)
