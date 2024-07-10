# 14. Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import date

fecha_inicio = date(2014,7,2)

fecha_fin = date(2014,7,11)

diferencia=str(abs(fecha_inicio - fecha_fin).days)


print('La diferencia entre las fechas es de '+ diferencia + ' días.')