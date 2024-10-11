import pytest
from calculadora import *

#Testes para soma
def test_soma_positivo():
    assert soma(2, 5) == 7

def test_soma_negativo():
    assert soma(2, -5) == -3

def test_soma_zero():
    assert soma(2, 0) == 2

#Testes para subtração
def test_subtracao_positivo():
    assert subtracao(5, 2) == 3

def test_subtracao_zero():
    assert subtracao(0, 2) == -2

def test_subtracao_negativo():
    assert subtracao(5, -2) == 7

#Testes para multiplicação
def test_multiplicacao_positivo():
    assert multiplicacao(5, 2) == 10

def test_multiplicacao_negativo():
    assert multiplicacao(5, -2) == -10

def test_multiplicacao_zero():
    assert multiplicacao(5, 0) == 0

#Testes para divisão
def test_divisao_positivo():
    assert divisao(6, 2) == 3

def test_divisao_negativo():
    assert divisao(6, -2) == -3

def test_divisao_zero():
    with pytest.raises(ValueError):
        divisao(6, 0)

#Testes para fatorial
def test_fatorial_positivo():
    assert fatorial(5) == 120

def test_fatorial_zero():
    assert fatorial(0) == 1

def test_fatorial_maior_que_zero():
    assert fatorial(5) > 0

def test_fatorial_nao_negativo():
    assert not fatorial(5) < 0

#Testes para potenciação
def test_potencia_positivo():
    assert potencia(6, 2) == 36

def test_potencia_negativo():
    assert potencia(6, -2) == 36

def test_potencia_zero():
    assert potencia(6, 0) == 1

def test_potencia_base_negativa_expoente_par():
    assert potencia(-2, 2) == 4

def test_potencia_base_negativa_expoente_impar():
    assert potencia(-2, 3) == -8