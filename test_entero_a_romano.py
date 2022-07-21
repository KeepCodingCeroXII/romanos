from romanos_funcional import entero_a_romano, romano_a_entero

"""
Casos de prueba 
a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberError("El valor debe ser menor de 4000")
c) "unacadena" -> RomanNumberError("Debe ser un entero")
d) 0 -> RomanNumberError("El valor debe ser mayor de cero")
e) -3 -> RomanNumberError("El valor debe ser mayor de cero")
f) 4.5 -> RomanNumberError("Debe ser un entero")


"""

def test_1336():
    assert entero_a_romano(1336) == 'MCCCXXXVI'

def test_336(): 
    assert entero_a_romano(336) == 'CCCXXXVI'

def test_romano_a_entero_ordenados():
    assert romano_a_entero('I') == 1
    assert romano_a_entero('MDCCXIII') == 1713
