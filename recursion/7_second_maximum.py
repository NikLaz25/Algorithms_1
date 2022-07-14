# нахождение второго максимального числа в списке 
#(с учётом, что максимальных может быть несколько, если они равны)
def second_maximum(work_list, first_max=0, second_max=0):
    if len(work_list) == 0:
        return second_max
    elif work_list[0] > first_max:
        second_max, first_max = first_max, work_list[0]
    elif second_max < work_list[0] < first_max:
        second_max = work_list[0]

    second_max = second_maximum(work_list[1:], first_max, second_max)
    
    return second_max

work_list = [1, 2, 4, 5, 5, 3, 2, 1, 2, 3, 5, 7, 8, 8, 8]
print(second_maximum(work_list, max(work_list), min(work_list)))
