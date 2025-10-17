from Pessoa import Pessoa;

class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, endereco, telefone, matricula):

        super().__init__(nome, idade, cpf, endereco, telefone)
        self.matricula = matricula
    
    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f'''    Matricula: {self.matricula}
''')