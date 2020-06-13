import graficoooooo as graf
import bibliotecaaaaaa as bib
import matplotlib.pyplot as plt
import numpy as np

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
        else:
            break
    anos = [1991, 2000, 2010]
    df = graf.gera_novo_dataframe(anos, data, estados, tipo_informacao)

    if grafico == 1:
        graf.gera_grafico_linhas(tipo_informacao)
    elif grafico == 2:
        barWidth = 0.25
        plt.figure(figsize=(10, 5))
        posicao = np.arange(len(estados))
        for i in range(len(estados)):
            df_aux = df[(df['estado'] == estados[i])]
            plt.bar(posicao, df_aux['media'], width=barWidth, color=cores[i],
                    label=bib.sigla_estado_to_nome(estados[i]))
            posicao = [x + barWidth for x in posicao]
        plt.xlabel('Anos')
        plt.xticks([r + barWidth for r in range(len(anos))], anos)
        plt.ylabel('Média')
        plt.title(f'{bib.sigla_tipo_to_descricao(tipo_informacao)} x Média dos Estados')
        plt.legend()
        plt.show()

        # graf.gera_grafico_barras(anos, estados, df, cores, tipo_informacao)

# estado = input('Digite a sigla do Estado')
# media = input('Escolhe o dado que queira ver')
# tipo_de_grafico = input('Qual grafico deseja exibir, Linhas ou Barras?')
# cor = input('Escolhe a cor do Grafico')

# estado = escolhe_estado(estado)

# sc = data[data.UF == 42]
# pr = data[data.UF == 41]
# rs = data[data.UF == 43]
# mort_inf_sc = sc['MORT1'].apply(lambda x: float(x.replace(".", "").replace(",", ".")))
# mort_inf_pr = pr['MORT1'].apply(lambda x: float(x.replace(".", "").replace(",", ".")))
# mort_inf_rs = rs['MORT1'].apply(lambda x: float(x.replace(".", "").replace(",", ".")))
# cidades = sc['UF']
#
# # plt.figure(figsize=(10,5))
# # chart = sns.barplot(
# #     data=sc,
# #     x='MORT1',
# #     palette='Set1'
# # )
# # chart.set_xticklabels(chart.get_xticklabels(), rotation=45, horizontalalignment='right')
# plt.title('Distribuição de Pesos')
#
# plt.figure(figsize=(10, 20))
# plt.bar(cidades, mort_inf_sc, color='red')
# plt.yticks(mort_inf_sc)
# plt.ylabel('Mortalidade Infantil')
#
# plt.xlabel('Cidades')
# # plt.hist(mort_inf_sc, bins=range(10, 16), rwidth=0.01,
# #          label='Santa Catarina', color='#000080')
# # plt.hist(mort_inf_pr, bins=range(12, 16), rwidth=0.01,
# #          label='Paraná', color='#2DB200')
# # plt.hist(mort_inf_rs, bins=range(12, 16), rwidth=0.01,
# #          label='Rio Grande do Sul', color='#ED4E20')
# # plt.legend(loc='upper right')
