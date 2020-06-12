def contratar_terceiros(qt_contratatos, qt_terceirizados, qt_ferias):
    total_nominal = qt_contratatos + qt_terceirizados
    total_disponivel = qt_contratatos + qt_terceirizados - qt_ferias
    contratar = 0
    if total_disponivel < (0.9 * total_nominal):
        contratar = qt_ferias / 2
        if contratar < (0.1 * qt_contratatos):
            contratar = 0.1 * qt_contratatos
    return contratar


funcoes = [["Finanças", [19, 10, 8]], ["Engenharia", [56, 9, 17]], ["REc. Humanos", [38, 4, 9]],
           ["Transporte", [12, 15, 5]], ["Adiministração", [86, 28, 13]]]

for funcao in (funcoes):
    print(
        f"É necessario contratar {contratar_terceiros(funcao[1][0], funcao[1][1], funcao[1][2])} para a área {funcao[0]}")
