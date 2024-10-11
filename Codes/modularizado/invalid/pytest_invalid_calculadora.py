import pytest
from calculadora import *


#Testes para soma
def test_soma_tipos_invalidos():
    with pytest.raises(TypeError):
        soma("a", 1)

def test_soma_com_none():
    with pytest.raises(TypeError):
        soma(1, None)

#Testes para subtração
def test_subtracao_tipos_invalidos():
    with pytest.raises(TypeError):
        subtracao("a", 1)

def test_subtracao_com_lista():
    with pytest.raises(TypeError):
        subtracao(10, [])

#Testes para multiplicação
def test_multiplicacao_tipos_invalidos():
    with pytest.raises(TypeError):
        multiplicacao("a", 1)


#Testes para divisão
def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)

def test_divisao_tipos_invalidos():
    with pytest.raises(TypeError):
        divisao("a", 1)

def test_divisao_com_string():
    with pytest.raises(TypeError):
        divisao(10, "5")

#Testes para potência
def test_potencia_base_zero_expoente_negativo():
    with pytest.raises(ZeroDivisionError):
        potencia(0, -1)

def test_potencia_tipos_invalidos():
    with pytest.raises(TypeError):
        potencia("a", 1)

def test_potencia_expoente_string():
    with pytest.raises(TypeError):
        potencia(5, "2")

def test_potencia_zero_com_zero():
    with pytest.raises(ValueError):
        potencia(0, 0)

#Testes para fatorial
def test_fatorial_negativo():
    with pytest.raises(ValueError):
        fatorial(-5)

def test_fatorial_decimal():
    with pytest.raises(TypeError):
        fatorial(3.5)

def test_fatorial_zero():
    assert fatorial(0) == 1

def test_fatorial_positivo():
    assert fatorial(5) == 120

