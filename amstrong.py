"""
Escribe una función que calcule si un número dado es un número de Armstrong
(o también llamado narcisista).
Si no conoces qué es un número de Armstrong, debes buscar información
al respecto.
"""


def isAmstrong(num1):
    # dividir el numero en cifras
    num_str = str(num1)
    listint = list(map(int, num_str))
    pontencia = len(listint)
    narciso = 0
    for cf in listint:
        # elevar cada cifra por el nummero de cifras
        narciso += cf**pontencia
    # verificar si es narcisista
    if narciso == num1:
        return True
    return False


ams = isAmstrong(153)
print(ams)
