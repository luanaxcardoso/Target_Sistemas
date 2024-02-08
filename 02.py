def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return True
    else:
        return False
    
n = int(input("Informe um número: "))

if fibonacci(n):
    print(f"O número {n} não faz parte da sequência Fibonacci")
    
else:
    print(f"O número {n} não faz parte da sequência Fibonacci")
    
