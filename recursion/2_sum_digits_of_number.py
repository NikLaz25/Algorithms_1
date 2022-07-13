# рекурсивный метод вычисление суммы цифр числа
def sum_digits_of_number(number):
    if len(str(number)) > 1:
        str_number = str(number)
        digit = int(str_number[0])
        remaining_number = int(str_number[1:])
        return digit + sum_digits_of_number(remaining_number)
    else:
        return number

sum_digits_of_number(333)
