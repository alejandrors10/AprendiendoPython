# 16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

num = int(input('Escribe tu número: '))

def calcularDif (n):

    if n > 17:

        return (17-n)*2
    else:
        return n-17
    
print(calcularDif(num))

