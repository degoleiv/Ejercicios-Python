# /*
#  * Crea una función que reciba dos cadenas como parámetro (str1, str2)
#  * e imprima otras dos cadenas como salida (out1, out2).
#  * - out1 contendrá todos los caracteres presentes en la str1 pero NO
#  *   estén presentes en str2.
#  * - out2 contendrá todos los caracteres presentes en la str2 pero NO
#  *   estén presentes en str1.
#  */

def delete_char (str1, str2):
    out1_list = [c for c in str2 if not c in str1]    
    out21_list = [c for c in str1 if not c in str2]    
    out1 = ''.join(out1_list)
    out2 = ''.join(out21_list)
    print(out1, out2)
    
    
delete_char("diana", "diego")