from Veiculo import Veiculo

class CaminhaoCarga(Veiculo):
    def __init__(self, marca, modelo, ano_publicacao, chassi, cor, quilometragem, capacidade_toneladas, eixos):
        self.capacidade_toneladas = capacidade_toneladas
        self.eixos = eixos
        super().__init__(marca, modelo, ano_publicacao, chassi, cor, quilometragem)

    def registrar_vistoria(self, motivo, multa):
        self.motivo = motivo
        self.multa = multa
        print(f'''Motivo: {self.motivo}
Multa: {self.multa}''')
        
    def exibir_informacoes(self):
        super().exibir_informacoes(True)
        print(f'''Toneldas: {self.capacidade_toneladas}
Eixos: {self.eixos}''')