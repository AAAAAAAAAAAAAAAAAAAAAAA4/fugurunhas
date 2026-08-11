FIGURINHAS_POR_PACOTE = 3

def calcular_desconto(quantidade_pacotes):
    if quantidade_pacotes >5:
        return 0.10
    elif quantidade_pacotes >2:
        return 0.05
    else:
        return 0
    
def realizar_vendas(filme, quantidade_albuns, quantidade_pacotes):
    total_albuns = quantidade_albuns * filme['preco_album']
    total_pacotes = quantidade_pacotes * filme['preco_pacote']

    percentual_desconto = calcular_desconto(quantidade_pacotes)
    valor_desconto = total_pacotes * percentual_desconto

    total_pacotes_com_desconto = total_pacotes - valor_desconto
    total_venda = total_albuns + total_pacotes_com_desconto

    venda = {
        "filme": filme['titulo'],
        "quantidade_albuns" : quantidade_albuns,
        "quantidade_pacotes" : quantidade_pacotes,
        "quantidade_figurinhas" : quantidade_pacotes * FIGURINHAS_POR_PACOTE,
        "total_albuns" : total_albuns,
        "total_pacotes" : total_pacotes,
        "percentual_desconto" : percentual_desconto,
        "valor_desconto" : valor_desconto,
        "total_venda" : total_venda
    }
    
    return venda
def exibir_venda(venda):
    print("\n - - - R E S U M O  D A  V E N D A - - - :")
    print(f"Fiilme: {venda['filme']}")
    print(f"Albuns: {venda['quantidade_albuns']}")
    print(f"Pacotes: {venda['quantidade_pacotes']}")
    print(f"Figorinhas: {venda['quantidade_figurinhas']}")
    print(f"Desconto: {venda['valor_desconto']:.2f}")
    print(f"Total da vanfa: R$ {venda['total_venda']:.2f}")