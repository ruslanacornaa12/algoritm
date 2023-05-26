def a_a(lst):
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst
print(a_a([1, 5, 77, 101, 10091]))
