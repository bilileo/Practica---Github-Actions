from Calculadora import Calculadora 
 
def test_add(): 
    calc = Calculadora() 
    assert calc.add(2, 3) == 5 

def test_restar():
    calc = Calculadora()
    resultado = calc.restar(5, 2)
    assert resultado == 3