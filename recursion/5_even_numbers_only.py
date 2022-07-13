# печать только чётных значений из списка
def even_numbers_only(work_list):
    if work_list and work_list[0] % 2 == 0 :
        print(work_list[0])
        even_numbers_only(work_list[1:])
    elif work_list and work_list[0] % 2 != 0 :
        even_numbers_only(work_list[1:])
    else:
        pass

work_list = [1, 2, 4, 3, 2, 1, 2, 3]
even_numbers_only(work_list)
