# нахождение второго максимального числа в списке 
#(с учётом, что максимальных может быть несколько, если они равны)
def second_maximum(work_list):
    if len(work_list) >= 3 and (work_list[2] == work_list[0] or work_list[2] == work_list[1]):
        del work_list[2]
        return second_maximum(work_list)

    elif len(work_list) >= 3 and work_list[1] < work_list[0] < work_list[2]:
        work_list[1] = work_list[0]
    elif len(work_list) >= 3 and work_list[0] < work_list[2] < work_list[1]:
        work_list[0] = work_list[2]
        work_list[2] = work_list[1]
        work_list[1] = work_list[0]
    elif len(work_list) >= 3 and work_list[1] < work_list[2] < work_list[0]:
        work_list[1] = work_list[2]
        work_list[2] = work_list[0]
    elif len(work_list) >= 3 and work_list[2] < work_list[0] < work_list[1]:
        work_list[2] = work_list[1]
        work_list[1] = work_list[0]
    elif len(work_list) >= 3 and work_list[2] < work_list[1] < work_list[0]:
        work_list[2] = work_list[0]    
    
    # завершение работы со списком
    elif len(work_list) == 2 and work_list[0] < work_list[1]:
        return work_list[0]
    elif len(work_list) == 2 and work_list[1] < work_list[0]:
        return work_list[1]
    elif len(work_list) < 2:
        print('Длина списка не соответствует требованиям')
        return
    
    return second_maximum(work_list[1:])

work_list = [1, 2, 4, 5, 5, 3, 2, 1, 2, 3, 5, 7, 8, 8, 8]
print(second_maximum(work_list))
