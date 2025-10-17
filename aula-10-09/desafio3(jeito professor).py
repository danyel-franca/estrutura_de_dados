
def exibir_cardapio():

    cardapio = {
        "Mussarela": 30.00,
        "Calabresa": 32.00,
        "Pepperoni": 35.00,
        "Quatro Queijos": 38.00,
        "Frango com Catupiry": 40.00
    }
    
    print("--- Cardápio da Pizzaria Sabores ---")
    for pizza, preco in cardapio.items(): #acessa a chave depois valor
        print(f"🍕 {pizza}: R$ {preco:.2f}")
    
    return cardapio


def receber_pedido(cardapio):

    pedido=[]

    while True:
        sabor = input("Escreva seu sabor de pizza: ")
        if sabor == 'sair':
            break
        elif sabor in cardapio:
            pedido.append(sabor)
            print(f"{sabor} foi adicionado ao pedido!")
        else:
            print("Seu pedido não existe!")
    return pedido


def calcular_pedido(pedido,cardapio):

    total = 0 
    for pizza in pedido:
        total += cardapio[pizza]
    return total


def main():

    cardapio = exibir_cardapio()
    pedido = receber_pedido(cardapio)
    total = calcular_pedido(pedido,cardapio)
    
    print("--- Resumo do peido ---")
    for pizza in pedido:
        print(f"{pizza} - R${cardapio[pizza]}")
    print(f"Total a pagar: R${total:.2f}")

main()