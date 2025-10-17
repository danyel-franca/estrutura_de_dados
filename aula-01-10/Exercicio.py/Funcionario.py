from Pessoa import Pessoa;

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, endereco, telefone, cargo):

        super().__init__(nome, idade, cpf, endereco, telefone)
        self.cargo = cargo

    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f'''    Cargo: {self.cargo}
''')