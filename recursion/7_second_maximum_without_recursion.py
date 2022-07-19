def second_maximum(work_list):
    first_max_value, second_max_value = work_list[0], work_list[0]

    for i in work_list:
        if i > first_max_value:
            first_max_value, second_max_value = i, first_max_value
        elif second_max_value < i < first_max_value or (first_max_value == second_max_value and i < second_max_value):
            second_max_value = i
    return second_max_value

work_list = [8, 2, 4, 5, 5, 3, 2, 2, 2, 3, 5, 7, 8, 8, 8]
second_maximum(work_list)
