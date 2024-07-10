# 19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".

a = input('Tu cadena de texto: ')

def modif_string(s):

    if len(s)>2 and s[:2]=='Is':
        return(s)
    else:
        return('Is '+s)

print(modif_string(a))