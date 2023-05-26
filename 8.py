def a_t(var1, var2):
    temp = var1
    var1 = var2
    var2 = temp
    return (var1, var2)
a = 1
b = 2
a, b = a_t(a,b)
print("a =",a)
print("b =",b)