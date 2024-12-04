
""" Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
 - Múltiplos de 3 por la palabra "fizz".
 - Múltiplos de 5 por la palabra "buzz".
 - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"."""
 
def fizzbuzz ():
    fizz = "fizz"
    buzz = "buzz" 
    for num in range(1, 101) :
        str = ""
        if num % 3 == 0 : 
            str = str + fizz
        if num % 5 == 0:
            str = str + buzz
            
        if str != "":
            print(str)
        else:    
            print (num)    
        
fizzbuzz


