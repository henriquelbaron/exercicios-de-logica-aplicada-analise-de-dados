import pandas as pd
import matplotlib.pyplot as plt
from Atlas_BR import biblioteca as bib
import numpy as np

data = bib.carregar_csv()

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
    rows = []

    for ano in anos:
        for estado in estados:
            linha_filtrada = data[(data.UF == estado) & (data.ANO == ano)]
            media = round(linha_filtrada[tipo_informacao].apply(
                lambda x: float(x.replace(".", "").replace(",", "."))).median(), 2)
            row = [estado, ano, media]
            rows.append(row)

    df = pd.DataFrame(columns=['estado', 'ano', 'media'])
    for row in rows:
        df.loc[-1] = row
        df.index = df.index + 1


    reacts = []
    x = np.arange(len(anos))
    width = 0.35
    fig, ax = plt.subplots()
    for i in range(len(estados)):
        df_aux = df[(df['estado'] == estados[i])]
        if grafico:
            plt.plot(df_aux['ano'], df_aux['media'])
        else:
            if (i % 2) == 0:
                rect = ax.bar(x - width/2, df_aux['media'], width, color=cores[i],
                              label=bib.sigla_estado_to_nome(estados[i]))
            else:
                rect = ax.bar(x + width/2, df_aux['media'], width, color=cores[i],
                              label=bib.sigla_estado_to_nome(estados[i]))

            reacts.append(rect)

    if not grafico:
        ax.set_ylabel('Média')
        ax.set_title(f'{bib.sigla_tipo_to_descricao(tipo_informacao)} x Média dos Estados')
        ax.set_xticks(x)
        ax.set_xticklabels(anos)
        ax.legend()
        for react_ in reacts:
            bib.autolabel(react_, ax)
        fig.tight_layout()
    else:
        plt.title(f'{bib.sigla_tipo_to_descricao(tipo_informacao)} x Média dos Estados')

    plt.show()

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
