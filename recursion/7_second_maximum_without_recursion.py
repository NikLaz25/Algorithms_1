def second_maximum(work_list):

    for x in range(2):
        max_value = work_list[0]
        for i in work_list:
            if i > max_value:
                max_value = i

        while max_value in work_list:
            work_list.remove(max_value)

    return max_value

work_list = [8, 2, 4, 5, 5, 3, 2, 2, 2, 3, 5, 7, 8, 8, 8]
second_maximum(work_list)
