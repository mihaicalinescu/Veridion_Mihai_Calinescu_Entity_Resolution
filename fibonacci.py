def fibonacci(n):
    fib = [0, 1]
    for _ in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def fibonacci2(n):
    fib = [0]
    a = 0
    b = 1
    for i in range (3, n):
        c = a + b
        a = b
        b = c
        fib.append(c)
    return fib

print (fibonacci(10))