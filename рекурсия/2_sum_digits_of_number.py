# рекурсивный метод вычисление суммы цифр числа
def sum_digits_of_number(number):
    if number > 0:
        digit = number % 10
        remaining_number = number // 10
        return digit + sum_digits_of_number(remaining_number)
    else:
        return number

sum_digits_of_number(333)
