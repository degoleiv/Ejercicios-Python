"""/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */"""

def invert_str (cadena):
    lista_cadena = list(cadena)
    cadena_inv = ""
    
    ultima_pos = len(lista_cadena)
    # recorrer la lista desde el ultimo hasta el primero 
    for i in range(0, ultima_pos):
        indice_inv = ultima_pos - (i + 1)
        cadena_inv = cadena_inv + lista_cadena[indice_inv]
    return cadena_inv

c_i = invert_str("Hola mi amor")
print(c_i)


















    

