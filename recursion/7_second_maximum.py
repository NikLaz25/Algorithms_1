# нахождение второго максимального числа в списке 
#(с учётом, что максимальных может быть несколько, если они равны)
def second_maximum(work_list):
    swapped = False
    for i in range(len(work_list) - 1):
        if work_list[i] > work_list[i + 1]:
            work_list[i], work_list[i + 1] = work_list[i + 1], work_list[i]
            swapped = True
    return second_maximum(work_list) if swapped else (list(set(work_list))[-2]) 

work_list = [1, 2, 4, 5, 5, 3, 2, 1, 2, 3, 5, 7, 8, 8, 8]
print(second_maximum(work_list))
