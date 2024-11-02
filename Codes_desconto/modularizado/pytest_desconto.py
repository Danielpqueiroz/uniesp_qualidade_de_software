import pytest
from desconto import *

def test_calcula_desconto_10():
    assert calcula_desconto(100, 10) == 90

def test_calcula_desconto_50():
    assert calcula_desconto(200, 50) == 100

def test_calcula_desconto_20():
    assert calcula_desconto(50, 20) == 40

def test_calcula_desconto_0():
    assert calcula_desconto(0, 15) == 0

def test_calcula_desconto_100():
    assert calcula_desconto(100, 0) == 100