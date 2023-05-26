def sum_a(n):
    sum = 0
    while n > 0:
        b = n % 10
        sum += b
        n = n // 10
    return sum
number = 1234567
print('сумма цифр', number, '=', sum_a(number))