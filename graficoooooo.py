import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import bibliotecaaaaaa as bib


# método que carrega dados a partir do CSV
def carregar_csv():
    data = pd.read_csv('atlas2013_dadosbrutos_pt.csv', sep='\t')
    return data

# cria um novo dataframe com o dados desejados
def gera_novo_dataframe(anos, data, estados, tipo_informacao):
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
    return df


def gera_grafico_barras(anos, estados, df, cores, tipo_informacao):
    reacts = []
    x = np.arange(len(anos))
    width = 0.35
    fig, ax = plt.subplots()
    for i in range(len(estados)):
        df_aux = df[(df['estado'] == estados[i])]
        if (i % 2) == 0:
            rect = ax.bar(x - width / 2, df_aux['media'], width, color=cores[i],
                          label=bib.sigla_estado_to_nome(estados[i]))
        else:
            rect = ax.bar(x + width / 2, df_aux['media'], width, color=cores[i],
                          label=bib.sigla_estado_to_nome(estados[i]))

        reacts.append(rect)

    ax.set_ylabel('Média')
    ax.set_title(f'{bib.sigla_tipo_to_descricao(tipo_informacao)} x Média dos Estados')
    ax.set_xticks(x)
    ax.set_xticklabels(anos)
    ax.legend()
    for react_ in reacts:
        for rect in react_:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    fig.tight_layout()
    plt.show()


def gera_grafico_linhas(tipo_informacao):
    plt.title(f'{bib.sigla_tipo_to_descricao(tipo_informacao)} x Média dos Estados')
    plt.show()
