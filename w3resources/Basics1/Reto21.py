# 21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

def even_odd(n):

    if n%2 == 0:
        return 'EL número es par'
    else:
        return 'El número es impar'
    
num = int(input('Introduce el número: '))

print(even_odd(num))