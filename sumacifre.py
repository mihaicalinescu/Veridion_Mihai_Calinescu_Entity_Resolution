def suma_cifre(n):
    return sum(int(cifra) for cifra in str(n))

def suma_cifre2(n):
    suma = 0
    while n >0 :
        suma = suma + n%10
        n = n // 10
    return suma

# print (suma_cifre(1234))
print (suma_cifre2(1234))