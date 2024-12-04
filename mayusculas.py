"""* Crea una función que reciba un String de cualquier tipo y se encargue de
* poner en mayúscula la primera letra de cada palabra.
* - No se pueden utilizar operaciones del lenguaje que
*   lo resuelvan directamente.
"""


def upper(str1):
    
    str_upperlist = []
    for char in str1:
        ascii_code = ord(char)
       
        if 97 <= ascii_code <= 122:
            if ascii_code != 32:
                ascii_code -= 32
       
            
        str_upperlist.append(chr(ascii_code))
    # # Join all the hex values into a single string
    str_upper = "".join(str_upperlist)
    return str_upper


st = upper("Hola mundo")
print(st)
