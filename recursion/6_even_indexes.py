# печать элементов списка с чётными индексами

def even_indexes(work_list, index=0):
    if index % 2 == 0:
        print(work_list[index])
    try:
        even_indexes(work_list, index + 1)
    except:
        pass

work_list = [1, 2, 4, 3, 2, 1, 2, 3]
even_indexes(work_list)