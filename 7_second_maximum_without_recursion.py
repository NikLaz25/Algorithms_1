# пузырьковая сортировка без рекурсии
def second_maximum(work_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(work_list) - 1):
            if work_list[i] > work_list[i + 1]:
                work_list[i], work_list[i + 1] = work_list[i + 1], work_list[i]
                swapped = True
    return (list(set(work_list))[-2])

work_list = [1, 2, 4, 5, 5, 3, 2, 2, 2, 3, 5, 7, 8, 8, 8]
second_maximum(work_list)