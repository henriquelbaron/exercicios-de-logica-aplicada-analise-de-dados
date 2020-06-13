import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import biblioteca as bib


# método que carrega dados a partir do CSV
def carregar_csv():
    data = pd.read_csv('atlas2013_dadosbrutos_pt.csv', sep='\t')
    return data


# cria um novo dataframe com o dados desejados
def gera_novo_dataframe(anos, data, estados, tipo_informacao):
    rows = []
    for ano in anos:
        for estado in estados:
            # filtra dataframe, como parametros o estado e o ano
            linha_filtrada = data[
                (data.UF == estado) & (data.ANO == ano)]
            # pega a linha que possui a informação escolhida, subistitui as , por .
            media = linha_filtrada[tipo_informacao].apply(lambda x: float(x.replace(".", "").replace(",", ".")))
            # pega a media do valores, e arredonda as casas decimais
            media = round(media.median(), 2)
            row = [estado, ano, media]
            rows.append(row)

    df = pd.DataFrame(columns=['estado', 'ano', 'media'])
    # adiciona as linhas no dataframe
    for row in rows:
        df.loc[-1] = row
        df.index = df.index + 1
    return df


def gera_grafico_barras(anos, estados, df, cores, tipo_informacao):
    barWidth = 0.25
    posicao = np.arange(len(anos))
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


def gera_grafico_linhas(anos, estados, df, cores, tipo_informacao):
    plt.title(f'{bib.sigla_tipo_to_descricao(tipo_informacao)} x Média dos Estados')
    for i in range(len(estados)):
        df_aux = df[(df['estado'] == estados[i])]
        plt.plot(df_aux['ano'], df_aux['media'], label=bib.sigla_estado_to_nome(estados[i]), color=cores[i])
    plt.xticks(anos)
    plt.xlabel('Anos')
    plt.ylabel('Média')
    plt.legend()
    plt.show()
