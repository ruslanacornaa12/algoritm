def a_b(n):
    a_b = 0
    while n > 0:
        b = n % 10
        a_b= (a_b * 10) + b
        n = n // 10
    return a_b
number = 123454
print("Перевернутое число", number, " =", a_b(number))