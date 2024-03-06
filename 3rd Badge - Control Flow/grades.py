import random

grade=random.randint(1,100)
print(grade)

nota="x"

if grade>=90:
    print("Sobresaliente")
elif grade>=70:
    print("Notable")
elif grade>=60:
    print("Bien")
elif grade>=50:
    print("Suficiente")
else:
    print("Suspenso")    