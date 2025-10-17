from Veiculo import Veiculo

class CarroPasseio(Veiculo):
    def __init__(self, marca, modelo, ano_publicacao, chassi, cor, quilometragem, numero_portas, tipo_combustivel):
        super().__init__(marca, modelo, ano_publicacao, chassi, cor, quilometragem)
        self.numero_portas = numero_portas
        self.tipo_combustivel = tipo_combustivel

    def calcular_depreciacao(self, anos_uso, taxa_extra):
        self.anos_uso = anos_uso
        self.taxa_extra = taxa_extra
        calculo = self.taxa_extra*self.anos_uso

        print(f"Depreciação: {calculo}")
    
    def exibir_informacoes(self):
        super().exibir_informacoes(True) 
        print(f'''Numero de portas: {self.numero_portas}
Combustível: {self.tipo_combustivel}''')