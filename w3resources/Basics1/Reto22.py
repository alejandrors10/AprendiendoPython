# 22. Write a Python program to count the number 4 in a given list.
count = 0
a = [1,2,3,4,5,8,6,4,3,4,6,1,4]

for fours in a:
    if fours == 4:
        count=count+1

print('El número 4 se repite '+str(count)+' veces.')
    