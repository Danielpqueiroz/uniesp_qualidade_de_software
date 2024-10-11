def calcula_desconto(preco, percentual):
    
    if preco < 0:
        raise ValueError("O preço não pode ser negativo.")
    if percentual < 0:
        raise ValueError("O percentual de desconto não pode ser negativo.")
    
    desconto = preco * (percentual / 100)
    novo_preco = preco - desconto
    
    if novo_preco < 0:
        return 0
    
    return novo_preco

