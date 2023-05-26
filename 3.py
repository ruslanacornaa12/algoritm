def a_q(c, d):
    b = []
    for number in range(c, d + 1):
        if number > 1:
            is_prime = True
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break

            if is_prime:
                b.append(number)

    return b
b = a_q(2, 100)
print("В диапазоне от 2 до 100 найдено", len(b), "простых чисел:")
print(b)