# Explicação da classe Veiculo:
        No começo coloquei a função "__init__" para inicializar 
    meus atributos, o self esta sendo usado para se referir ao pró-
    prio objeto. Embaixo, usei a expressão "self.atributo = atributo"
    para os atributos da classe Veiculo, estou atribuindo o valor que 
    foi passado como argumento ao atributo.
        Logo a baixo criei a função "registrar_manutencao", com a 
    mesma estrutura da função "__init__", de diferente coloquei um 
    print para os atributos dessa classe "registrar_manutencao".
        Criei a função "exibir_informacoes", nela utilizei a seguinte
    estrutura: Se o atributo 'detalhado' for 'False' a função fará
    um print dos atributos da função "__init__", que serão 'Marca', 
    'Modelo' e 'Quilometragem'. Se o atributo 'detalhado' for 'True' 
    a função fará um print de todos os atributos da função "__init__".
    No print eu coloco o "self." antes para me referir ao atributo da função.

# Explicação da classe CarroPasseio:
        Na primeira linha importei a classe 'pai' (Veiculo). Logo abaixo
    criei a classe 'CarroPasseio' e coloquei como parametro a classe 'Veiculo'
    para a herença. Fiz a função padrão '__init__', onde coloquei todos os atri-
    butos da classe herdada (Veiculo) e tambem novos atributos (numero_portas,
    tipo_combustivel). Logo após criei a estrutura 'super().__init__', para 
    informar que esses atributos são da classe 'pai' (Veiculo), embaixo fiz a estrutura 
    do 'self.' para os novos atributos da subclasse (CarroPasseio).
        Fiz a função 'calcular_depreciacao' que foi usados novos atributos 
    'anos_uso' e 'taxa_extra', logo abaixo criei a variavel 'calculo', que
    calcula a taxa de depreciação, na ultima linha da função coloquei um print
    para a variavel 'calculo'
        Por ultimo na classe, criei a função 'exibir_informacoes'. Como parametro
    coloco o self para se referir aos atributos da classe. Logo abaixo coloquei
    'super().exibir_informacoes(True)', ela foi usada para se referir a função
    'exibir_detalhes' da classe 'pai' (Veiculo), por isso o uso do 'super()'
    na frente e o 'True' como parametro para ser impresso todos os os 6 atributos
    pertencentes a classe 'Veiculo'. Embaixo fiz um print dos novos atributos 
    (numero_portas, tipo_combustivel), para ser listado junto dos outros 6 atributos,
    isso é o Polimorfismo.

# Explicação da classe CaminhaoCarga:
        Criei a classe 'CaminhaoCarga' passando como parametro a classe 'Veiculo'. 
    Da mesma forma que na classe 'CarroPasseio', crei a função '__init__' passando 
    como parametro os 6 atributos da herdada e colocando novos atributos (capacidade_toneladas, 
    eixos). No código em diante foi usado a mesma estrutura que na classe 'CarroPasseio',
    que ja foi explicado anteriormente.

# Explicação do arquivo main:
        Importei todas as classes 'Veiculo', 'CarroPasseio' e 'CaminhaoCarga'. Para teste 
    e demonstração criei objetos para cada tipo de classe e função.
        Para a classe 'Veiculo', criei o objeto 'veiculoPadrao', igualei a classe que ele pertence
    e passei como parametro suas respectivas informações, coloquei o print só para organização.
    Embaixo do print coloquei o objeto junto da função 'exibir_informacoes(True)', foi usado o True
    para que eles faça o print de todos os 6 atributos. Logo após fiz a variação da função sendo 
    'exibir_informacoes(False)' com parametro False imprimindo somente 'Marca', 'Modelo' e 'Quilometragem'.
    Depois usei o objeto 'veiculoPadrao' com a função 'registrar_manutencao' que foi passado seus respec-
    tivos parametros.
        Para a clsse 'CarroPasseio', criei o objeto 'veiculoPasseio', igualei a classe que ele pertence
    e passei seus parametros, com os herdados da classe 'pai' (Veiculo) junto dos novos 'numero_portas' e 
    'tipo_combustivel'. Logo após coloquei o objeto 'veiculoPasseio' com a função 'calcular_depreciacao',
    que precisa ser passado os parametros para o devido calcula da função.
        Para a clase 'CaminhaoCarga', criei o objeto 'veiculoCaminhao', igualei a classe que ele pertence
    e passei seus parametros, com os herdados da classe 'pai' (Veiculo) junto dos novos 'capacidade_toneladas' e 
    'eixos'. Logo após coloquei o objeto 'veiculoCaminhao' com a função 'registrar_vistoria' que foi passado seus respec-
    tivos parametros.
        Na parte do 'if __name__ == "__main__": main()' eu não sei explicar kkkkk, você ainda não explicou essa parte
    so disse para aceitarmos kkkk, desculpa!
    