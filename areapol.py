"""/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */"""


def area_pol (l1, l2, isTriangule = False):
    # SQUARE, RECTANGULE
    area = l1 * l2
    # TRIANGULE  
    if isTriangule:
        area = area / 2
    return area

area_tr = area_pol(2, 6, True)
area_sq = area_pol(2, 2, False)
area_rt = area_pol(2, 4)
