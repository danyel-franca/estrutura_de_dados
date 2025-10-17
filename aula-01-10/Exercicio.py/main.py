from Professor import Professor;
from Aluno import Aluno;
from Pessoa import Pessoa;
from Funcionario import Funcionario;


def main():

    pessoa = Pessoa("Danyel", 18, 343323543, "Rua meideiros", 2135645354)
    print('---Pessoa---')
    pessoa.mostrar_detalhes()
    
    professor = Professor("Aroldo", 47, 33245332, "Rua não sei", 343732832, "Matemática")
    print('---Professor---')
    professor.mostrar_detalhes()

    aluno = Aluno("Danyel", 18, 343323543, "Rua meideiros", 2135645354, 232432234)
    print('---Aluno---')
    aluno.mostrar_detalhes()

    funcionario = Funcionario("Diniz", 89, 3847829, "Rua aqui perto", 3826682, "Gerente")
    print('---Funcionário---')
    funcionario.mostrar_detalhes()

if __name__ == "__main__":
    main()