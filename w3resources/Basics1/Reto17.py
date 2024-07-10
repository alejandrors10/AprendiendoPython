# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

def alrededor_mil(n):

    return (abs(1000-n)<=100) or ((abs(2000-n)<=100))

num = int(input('Introduce tu número: '))

if alrededor_mil(num):

    print('El número está cerca de 1000 o 2000')
else:
    print('El número NO está cerca de 1000 o 2000')
    