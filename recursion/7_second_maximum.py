# нахождение второго максимального числа в списке 
#(с учётом, что максимальных может быть несколько, если они равны)
def second_maximum_recursion(work_list, first_max_value, second_max_value=None):
    '''рекурсивный метод нахождения второго максимума'''
    if work_list[0] == first_max_value:
        pass
    elif work_list[0] > first_max_value:
        first_max_value, second_max_value = work_list[0], first_max_value
    elif (work_list[0] < first_max_value and second_max_value is None) or second_max_value < work_list[0] < first_max_value:
        second_max_value = work_list[0]
    return second_max_value if len(work_list) == 1 else second_maximum_recursion(work_list[1:], first_max_value, second_max_value)

def second_maximum(work_list):
    '''нахождение второго максимального числа в списке'''
    if len(work_list) > 1:
        first_max_value  = work_list[0]
        second_max_value = second_maximum_recursion(work_list, first_max_value)
        return second_max_value
    else:
        return

work_list = [8, 2, 4, 5, 5, 3, 2, 1, 2, 3, 5, 7, 8, 8, 8]
print(second_maximum(work_list))
