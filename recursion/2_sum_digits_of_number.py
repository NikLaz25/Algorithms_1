# рекурсивный метод вычисление суммы цифр числа
def sum_digits_of_number(number):
    if len(str(number)) > 0:
        str_number = str(number)
        digit = int(str_number[0])
        try:
            remaining_number = int(str_number[1:])
            return digit + sum_digits_of_number(remaining_number)
        except:
            return digit

sum_digits_of_number(333)