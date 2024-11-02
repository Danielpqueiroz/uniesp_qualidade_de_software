import pytest
from desconto import *

def test_calcula_desconto_com_string():
    with pytest.raises(TypeError):
        calcula_desconto("cem", 10)

def test_calcula_desconto_com_percentual_negativo():
    with pytest.raises(ValueError):
        calcula_desconto(100, -10)

def test_calcula_desconto_com_preco_negativo():
    with pytest.raises(ValueError):
        calcula_desconto(-100, 10)
        
def test_calcula_desconto_percentual_maior_que_cem():
    assert calcula_desconto(100, 150) == 0, "Preço final não deve ser negativo mesmo com desconto maior que 100%"
