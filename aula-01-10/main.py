from PizzaPadrao import PizzaPadrao; from PizzaDoce import PizzaDoce

def main():

    pizza_mussarela = PizzaPadrao("Mussarela", "Pequena", 29.90, "Queijo, molho de tomate, massa")
    pizza_mussarela.mostrar_detalhes()

    pizza_calabresa = PizzaPadrao("Calabresa", "Grande", 55.00, "Queijo, tomate, calabresa")
    pizza_calabresa.mostrar_detalhes()

    pizza_comum = PizzaPadrao("Calabresa", "Família", 29.90, "Tomate, cebola")
    print("--- Pizza comum ---")
    pizza_comum.mostrar_detalhes()

    pizza_chocolate = PizzaDoce("Chocolate com morango", "Pequena", 31.90, "Chocolate, massa, morango", "Chocolate")
    print("--- Pizza doce ---")
    pizza_chocolate.mostrar_detalhes()

if __name__ == "__main__": # "Se o nome for main, execute ele"
    main()