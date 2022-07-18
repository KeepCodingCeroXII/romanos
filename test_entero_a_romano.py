from first_part import entero_a_romano

"""
Casos de prueba 
a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberError("El valor debe ser menor de 4000")
c) "unacadena" -> RomanNumberError("Debe ser un entero")
d) 0 -> RomanNumberError("El valor debe ser mayor de cero")
e) -3 -> RomanNumberError("El valor debe ser mayor de cero")
f) 4.5 -> RomanNumberError("Debe ser un entero")


"""

def test_3_es_igual_a_2_mas_uno():
    assert 2 + 1 == 3 


def test_valor_1994():
    assert entero_a_romano(1994) == 'MCMXCIV' 

def test_valor_1995():
    assert entero_a_romano(1995) == 'MCMXCV' 
