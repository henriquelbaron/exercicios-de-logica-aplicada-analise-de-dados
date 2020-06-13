import grafico as graf
import biblioteca as bib

data = graf.carregar_csv()

while True:
    bib.imprime_opcoes_tipo_grafico()
    grafico = bib.escolhe_tipo_grafico(input())
    bib.imprime_opcoes_tipo_informacao()
    tipo_informacao = bib.escolhe_tipo_informacao(input())
    estados = []
    cores = []
    while True:
        bib.imprime_opcoes_estados()
        opcao_estado = bib.escolhe_estado(input())
        if opcao_estado != 0:
            bib.imprime_opcoes_cores()
            opcao_cor = bib.escolhe_cor(input())
            estados.append(opcao_estado)
            cores.append(opcao_cor)
        elif not estados:
            print('Escolha ao menos Um Estado e Uma Cor')
        else:
            break
    anos = [1991, 2000, 2010]
    df = graf.gera_novo_dataframe(anos, data, estados, tipo_informacao)

    if grafico == 1:
        graf.gera_grafico_linhas(anos, estados, df, cores, tipo_informacao)
    elif grafico == 2:
        graf.gera_grafico_barras(anos, estados, df, cores, tipo_informacao)
