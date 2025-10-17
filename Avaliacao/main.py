from Veiculo import Veiculo
from CarroPasseio import CarroPasseio
from CaminhaoCarga import CaminhaoCarga

def main():

    # Classe Veiculo
    veiculoPadrao = Veiculo("Fiat", "gol", 2013, "23131", "Preto", 29.932)
    print("-----Veiculo Padrão (True)-----")
    veiculoPadrao.exibir_informacoes(True)

    print("\n-----Veiculo Padrão (False)----")
    veiculoPadrao.exibir_informacoes(False)

    print("\n-----Veiculo Padrão (Manutenção)-----")
    veiculoPadrao.registrar_manutencao("Pneu furado", 2000)

    # Classe CarroPasseio
    veiculoPasseio = CarroPasseio("Ferrari", "Spider", 2020, "28232", "Vermelha", 19263.00, 2, "Gasolina")
    print("\n----Veiculo Passeio(Sem depreciação)----")
    veiculoPasseio.exibir_informacoes()

    print("\n----Depreciação do Veiculo Passeio----")
    veiculoPasseio.calcular_depreciacao(20,10)

    # Classe CaminhaoCarga
    veiculoCaminhao = CaminhaoCarga("Mercedez", "Truck", 2024, "273272", "Branco", 52837.00, 5, 4)
    print("\n----Veiculo Caminhão(Sem vistoria)----")
    veiculoCaminhao.exibir_informacoes()

    print("\n----Vistoria do Veiculo Caminhão----")
    veiculoCaminhao.registrar_vistoria("Embreagado", 1000)

if __name__ == "__main__":
    main()