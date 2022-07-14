# печать элементов списка с чётными индексами
def even_indexes(work_list, index=0):
    if index == len(work_list):
        return
    elif index < len(work_list) and index % 2 == 0:
        print(work_list[index])

    even_indexes(work_list, index + 1)

work_list = [1, 2, 4, 3, 2, 1, 2, 3]
even_indexes(work_list)
