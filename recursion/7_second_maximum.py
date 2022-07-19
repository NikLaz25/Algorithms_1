# нахождение второго максимального числа в списке 
#(с учётом, что максимальных может быть несколько, если они равны)

def second_maximum_recursion(work_list, function_call_count):
    '''рекурсивный метод нахождения максимума, ограничен двумя итерациями'''
    max_value = work_list[0]
    for i in work_list:
        if i > max_value:
            max_value = i

    while max_value in work_list:
        work_list.remove(max_value)

    return max_value if function_call_count >= 2 else  second_maximum_recursion(work_list, function_call_count + 1)

def second_maximum(work_list):
    '''нахождение второго максимального числа в списке'''
    second_max_value = second_maximum_recursion(work_list, 1)
    return second_max_value

work_list = [8, 2, 4, 5, 5, 3, 2, 1, 2, 3, 5, 7, 8, 8, 8]
print(second_maximum(work_list))
