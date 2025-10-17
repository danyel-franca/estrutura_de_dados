#dicionario
pedidos = {}

cardapio = {
    "mussarela": 25.90,
    "calabresa": 27.90,
    "frango com catupiry": 29.90,
    "portuguesa": 30.90,
    "alho": 30.00
}

while True:
    
    comando = input('''
CARDÁPIO!!
Mussarela: 25.90
Calabresa: 27.90
Frango com catupiry: 29.90
Portuguesa: 30.90
Alho: 30.00
Digite 'sair' para encerrar
Escolha seu sabor: ''').lower()
    
    if comando == 'sair':
        print(f"Seu pedido final foi {pedidos} com preço final de R${somador}")
        break

    if comando in cardapio:

        # adicionar somente um item de um dicionario a outro
        pedidos [comando] = cardapio [comando]
        
        # somar itens do dicionario
        somador = sum(pedidos.values()) 

        print(f"Seu cardápio até o momento é {pedidos}")

    else:
        print("Seu pedido não esta no cardápio!!")




