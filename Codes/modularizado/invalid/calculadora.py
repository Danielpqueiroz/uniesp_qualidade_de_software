
    
def soma(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Ambos os argumentos devem ser números")
    return a + b

def subtracao(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Ambos os argumentos devem ser números")
    return a - b

def multiplicacao(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Ambos os argumentos devem ser números")
    return a * b

def divisao(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Ambos os argumentos devem ser números")
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def potencia(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Ambos os argumentos devem ser números")
    if a == 0 and b == 0:
        raise ValueError("0 elevado a 0 não é definido")
    return a ** b
    
def fatorial(n):
    if n < 0:
        raise ValueError("Fatorial não definido para números negativos")
    if not isinstance(n, int):
        raise TypeError("Fatorial só é definido para números inteiros")
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)




