
"""/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */"""


def dec_to_binary(number):
    binary=""
    if number == 0:
        return 0
    while number > 0:
        res= number % 2
        number = int(number / 2) 
        binary = f"{res}{binary}" 
    return binary   
bin = dec_to_binary(2)

print(bin)