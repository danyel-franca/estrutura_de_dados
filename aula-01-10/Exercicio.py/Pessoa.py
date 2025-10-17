class Pessoa:
    def __init__(self, nome, idade, cpf, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    def mostrar_detalhes(self):
        print(f'''
    Nome: {self.nome}
    Idade: {self.idade}
    Cpf: {self.cpf}
    Endereço:  {self.endereco}
    Telefone: {self.telefone}''')
    
