# нахождение второго максимального числа в списке 
#(с учётом, что максимальных может быть несколько, если они равны)
def second_maximum(work_list, first_max, second_max):
    
    if len(work_list) == 0:
        return second_max
    elif len(work_list) != 0 and work_list[0] < first_max and work_list[0] > second_max:
        second_max = work_list[0]
    elif len(work_list) != 0 and work_list[0] < first_max and work_list[0] <= second_max:
        pass

    second_max = second_maximum(work_list[1:], first_max, second_max)

    return second_max

work_list = [-1, -2, -4, -5, -5, -1]
print(second_maximum(work_list, max(work_list), min(work_list)))

work_list = [1, 2, 4, 5, 5, 3, 2, 1, 2, 3, 5, 7, 8, 8, 8]
print(second_maximum(work_list, max(work_list), min(work_list)))
