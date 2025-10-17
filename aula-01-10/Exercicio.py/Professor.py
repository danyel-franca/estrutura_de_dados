from Pessoa import Pessoa;

class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, endereco, telefone, disciplina):

        super().__init__(nome, idade, cpf, endereco, telefone)
        self.disciplina = disciplina

    def mostrar_detalhes(self):
        super().mostrar_detalhes()
        print(f'''    Disciplina: {self.disciplina}
''')