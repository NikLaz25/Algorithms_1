# поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности

def file_search(catalog_name):

    # получим список объектов в заданном каталоге
    content = os.listdir(catalog_name)

    # переформатируем список объектов в список адресов
    adres_list = []
    for i in content:
        i_adres = os.path.join(catalog_name, i)
        adres_list.append(i_adres)

    # разобъём объекты на список адресов папок и адресов файлов
    file_adres_list = []
    folder_adres_list = []
    for i in adres_list:
        if os.path.isfile(i) is True:
            file_adres_list.append(i)
        else:
            folder_adres_list.append(i)

    # ЦИКЛ пополним file_list файлами из текущей директории
    file_list=[]
    for i in file_adres_list:
        file_name = os.path.basename(i)
        file_list.append(file_name)

    # ЦИКЛом для каждой папки вызовем рекурсивный метод 
    # и добавим результат в file_list
    for i in folder_adres_list:
        file_list_for_folder = file_search(i)
        file_list += file_list_for_folder
    
    return file_list

adres = r'C:\Users\lazarevnv\OneDrive\1_Обучение\Алгоритмы\рекурсия'
print(file_search(adres))