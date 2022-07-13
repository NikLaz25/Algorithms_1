# нахождение второго максимального числа в списке (с учётом, что максимальных может быть несколько, если они равны)

def second_maximum(work_list, max_in_list):
    work_list = sorted(work_list)[::-1]
    if work_list[0] == max_in_list:
        work_list = work_list[1:]
        return second_maximum(work_list, max_in_list)
    else:
        return work_list[0]

work_list = [1, 2, 4, 5, 5, 3, 9, 2, 1, 2, 9, 3, 5, 7, 8, 8, 8]
second_maximum(work_list, max(work_list))