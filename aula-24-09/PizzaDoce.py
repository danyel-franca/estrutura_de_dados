# Classe filha - subclass()

from PizzaPadrao import PizzaPadrao; # Importar a classe se outro arquivo

class PizzaDoce(PizzaPadrao): # Instanciando a classe "PizzaPadrao" dentro da sub-classe, para herdar atributos e métodos da classe Pai "PizzaPadrao"
    
    def __init__(self, sabor, tamanho, preco, ingredientes, borda_recheada): # "borda_recheada" é um atributo novo da subclasse PizzaDoce 
        
        super().__init__(sabor, tamanho, preco, ingredientes) # Para referir que esses atributos são da classe PizzaPadrao!
        
        self.borda_recheada = borda_recheada # Para o atributo que é novo, o atributo que so a PizzaDoce tem
    

    # Polimorfismo (Sobrescrita)
    def mostrar_detalhes(self): # Se eu usar algum atributo que esta no construtor, eu coloco self como parametro
                                # Puxando o método "mostrar_detalhes()", que é da classe PizzaPadrao

        super().mostrar_detalhes() # Método da classe "PizzaPadrao", será mostrado oque está no codigo da classe "PizzaPadrao"

        print(f'''        Borda recheada: {self.borda_recheada}''') # Adicionando mais informação ao método "mostrar_detalhes()"


# Criando Objetos

pizza_comum = PizzaPadrao("Calabresa", "Família", 29.90, "Tomate, cebola")

pizza_chocolate = PizzaDoce("Chocolate com morango", "Pequena", 31.90, "Chocolate, massa, morango", "Chocolate")

print("--- Pizza comum ---")
pizza_comum.mostrar_detalhes() # Em "pizza_comum" tenho um construtor com 4 instancias

print("--- Pizza doce ---")
pizza_chocolate.mostrar_detalhes() # Em "pizza_chocolate" tenho um construtor com 5 instancias, por conta da "sobrescrita", adicionamos "borda_recheada"

