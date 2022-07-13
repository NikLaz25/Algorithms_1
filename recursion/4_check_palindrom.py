# проверка, является ли строка палиндромом

def check_palindrom(palindrom):
    if palindrom == '':
        return True

    elif len(palindrom) > 0 and palindrom[0] == palindrom[-1]:
        return check_palindrom(palindrom[1:-1])

    elif len(palindrom) > 0 and palindrom[0] != palindrom[-1]:
        return False

    else:
        return True

palindrom = 'my123_321ym'
print(check_palindrom(palindrom))