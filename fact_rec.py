# # /*
# #  * Escribe una función que calcule y retorne el factorial de un número dado
# #  * de forma recursiva.
# #  */


def factorial(num):
    if num > 0:
        res = num * factorial(num - 1)
        return res
    return 1


fact = factorial(10)
print(fact)
