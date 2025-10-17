# Classe pai - SuperClass()
class PizzaPadrao:
    def __init__(self, sabor, tamanho, preco, ingredientes):
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco = preco
        self.ingredientes = ingredientes
        
    def mostrar_detalhes(self): # Se eu usar algum atributo que esta no construtor, eu coloco self como parametro
        print(f'''
"--- Detralhes da pizza ---"
        Sabor: {self.sabor}
        Tamanho:{self.tamanho}
        Preço: {self.preco}
        Ingredientes: {self.ingredientes}''')
        
pizza_mussarela = PizzaPadrao("Mussarela", "Pequena", 29.90, "Queijo, molho de tomate, massa")
pizza_calabresa = PizzaPadrao("Calabresa", "Grande", 55.00, "Queijo, tomate, calabresa")
pizza_calabresa.mostrar_detalhes()
pizza_mussarela.mostrar_detalhes()