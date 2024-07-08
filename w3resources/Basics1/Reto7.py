# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

a = input("Introduce el nombre del archivo: ")
ext = a.split('.')
print('La extensión del archivo es ' + repr(ext[1]))