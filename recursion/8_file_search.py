# поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности
import os

def file_search(catalog_name):
    # Создаём локальный список  и заносим в него все файлы в текущем каталоге.
    file_list = [i for i in os.listdir(catalog_name) if os.path.isfile(os.path.join(catalog_name, i))]
    # Цикл, для каждого из подкаталогов текущего каталога  
    for i in [(os.path.join(catalog_name, i)) for i in (os.listdir(catalog_name)) if (os.path.isdir(os.path.join(catalog_name, i)))]:
        file_list_for_folder = file_search(i) # вызываем рекурсивно функцию, которая возвращает файлы в указанном подкаталоге.
        file_list += file_list_for_folder # добавляем их в список 

    # Цикл закончился — делаем return
    return file_list

adres = r'C:\Users\lazarevnv\OneDrive\1_Обучение\Алгоритмы\рекурсия'
print(file_search(adres))
