class Pizza:
    
    # Atributos da Classe (Construtor padrão), construtor é um tipo de função!
    def __init__(self, sabor, tamanho, preco):  # Para declarar os atributos eles precisam estar nesta classe   # Colocar self em primeiro sempre antes dos atributos
        self.sabor = sabor # Igual em java (this.variavel = variavel)
        self.tamanho = tamanho
        self.preco = preco

    # Método descrever
    def descricao(self): # Se eu usar algum atributo que esta no construtor, eu coloco self como parametro
        return f"Pizza de {self.sabor}, Tamanho: {self.tamanho}, Preço: R$ {self.preco:.2f}"

# Criando objetos da classe Pizza
pizza1 = Pizza("Calabresa", "Família", 52.00) # O Python ja reconhece que você esta se referindo ao construtor, por conta do "__init__"
pizza2 = Pizza("Mussarela", "Média", 49.90)

print(pizza1.descricao()) # Para executar e printar a função "descricao" com o objeto "pizza1"
print(pizza2.descricao())