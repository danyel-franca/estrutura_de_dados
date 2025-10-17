
class Veiculo:
    def __init__(self, marca, modelo, ano_publicacao, chassi, cor, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano_publicacao = ano_publicacao
        self.chassi = chassi
        self.cor = cor
        self.quilometragem = quilometragem
    
    def registrar_manutencao(self, tipo, custo):
        self.tipo = tipo
        self.custo = custo
        print(f'''Tipo: {self.tipo}
Custo: {self.custo}''')
        
    def exibir_informacoes(self, detalhado):
        if detalhado == False:
            print(f'''Marca: {self.marca}
Modelo: {self.modelo}
Quilometragem: {self.quilometragem}''')
            
        else:
            print(f'''Marca: {self.marca}  
Modelo: {self.modelo}
Ano de publicação: {self.ano_publicacao}
Quilometragem: {self.quilometragem}
Chassi: {self.chassi}
Cor: {self.cor}''')

