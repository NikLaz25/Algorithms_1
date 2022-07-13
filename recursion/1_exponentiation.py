# рекурсивный метод возведения в степень
def exponentiation(number, extent):
    if extent > 0:
        return number * exponentiation(number, extent - 1)
    else:
        return 1

exponentiation(3, 3)