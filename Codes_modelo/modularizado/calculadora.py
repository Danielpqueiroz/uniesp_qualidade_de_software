
    
def soma(a, b):
    soma = a + b
    return soma

def subtracao(a, b):
    subtracao = a - b
    return subtracao

def multiplicacao(a, b):
    multiplicacao = a * b
    return multiplicacao

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def potencia(a, b):
    potencia = a ** b
    return potencia

