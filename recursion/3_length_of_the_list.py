# расчёт длины списка, для которого разрешена только одна операция удаления первого элемента pop(0)

def length_of_the_list(work_list):
    try:
        work_list.pop(0)
        return 1 + length_of_the_list(work_list)
    except:
        return 0

work_list = [1, 2, 4, 3, 2, 1, 2]
length_of_the_list(work_list)