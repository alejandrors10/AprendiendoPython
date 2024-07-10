# 18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

def magic_calc(m,n,o):

    if m == n == o:
        return (m+n+o)*3
    else:
        return m+n+o

num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))
num3 = int(input('Introduce el tercer número: '))

print(magic_calc(num1,num2,num3))

