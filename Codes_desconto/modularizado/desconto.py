def calcula_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    novo_preco = preco - desconto
    return novo_preco
