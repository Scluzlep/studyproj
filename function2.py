def is_narcissistic(n):
    if n < 100 or n >= 1000:
        return False
    elif 100 <= n < 1000:
        if int(str(n)[0])**3 + int(str(n)[1])**3 + int(str(n)[2])**3 == n:
            return True
        else:
            return False


print(is_narcissistic(int(input('输入一个三位数'))))
