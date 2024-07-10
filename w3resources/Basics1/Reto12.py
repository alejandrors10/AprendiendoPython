# 12. Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.

import calendar

y = int(input('¿Qué año? '))
m = int(input('¿Qué mes? '))

print(calendar.month(theyear=y,themonth=m))
