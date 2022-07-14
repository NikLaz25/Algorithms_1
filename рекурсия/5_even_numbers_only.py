# печать только чётных значений из списка
def even_numbers_only(work_list):
    if len(work_list) == 0:
        return
    elif work_list[0] % 2 == 0 :
        print(work_list[0])
    even_numbers_only(work_list[1:])

work_list = [1, 2, 4, 3, 2, 1, 2, 3]
even_numbers_only(work_list)
