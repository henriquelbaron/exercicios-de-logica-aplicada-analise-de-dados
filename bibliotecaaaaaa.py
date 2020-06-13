

def escolhe_tipo_grafico(argumento):
    switcher = {
        '1': 1,
        '2': 2
    }
    if switcher.get(argumento, True):
        print("Escolha um opção Valida")
        escolhe_tipo_grafico(input())
    return switcher.get(argumento)


def imprime_opcoes_tipo_grafico():
    print('\n' * 50)
    print('******* ESCOLHA TIPO DO GRAFICO *******')
    print('* <1> Linha                           *')
    print('* <2> Barras                          *')
    print('***************************************')


def escolhe_tipo_informacao(argumento):
    switcher = {
        '1': 'ESPVIDA',
        '2': 'FECTOT',
        '3': 'MORT1',
        '4': 'MORT5'
    }
    if switcher.get(argumento, True):
        print("Escolha um opção Valida")
        escolhe_tipo_informacao(input())
    return switcher.get(argumento)


def imprime_opcoes_tipo_informacao():
    print('\n' * 50)
    print('************* ESCOLHA A INFORMAÇÃO DO GRAFICO ************')
    print('* <1> Esperança de vida ao nascer                        *')
    print('* <2> Taxa de fecundidade total                          *')
    print('* <3> Mortalidade infantil                               *')
    print('* <4> Mortalidade até 5 anos de idade                    *')
    print('**********************************************************')


def sigla_tipo_to_descricao(argumento):
    switcher = {
        'ESPVIDA': 'Esperança de vida ao nascer ',
        'FECTOT': 'Taxa de fecundidade total',
        'MORT1': 'Mortalidade até um ano de idade',
        'MORT5': 'Mortalidade até cinco anos de idade'
    }
    return switcher.get(argumento, "Opção Inválida")


def escolhe_cor(argumento):
    switcher = {
        '1': '#000000',
        '2': '#4F4F4F',
        '3': '#000080',
        '4': '#00FFFF',
        '5': '#00FF00',
        '6': '#A0522D',
        '7': '#FF00FF'
    }
    if switcher.get(argumento, True):
        print("Escolha um opção Valida")
        escolhe_cor(input())
    return switcher.get(argumento)


def imprime_opcoes_cores():
    print('\n' * 50)
    print('************* ESCOLHA UMA COR *************')
    print('* <1> Preto                               *')
    print('* <2> Cinza                               *')
    print('* <3> Azul Marinho                        *')
    print('* <4> Azul Claro                          *')
    print('* <5> Verde                               *')
    print('* <6> Marron                              *')
    print('* <7> Roxo                                *')
    print('*******************************************')


def escolhe_estado(argumento):
    switcher = {
        '1': 41,
        '2': 43,
        '3': 42,
        '4': 35,
        '5': 32,
        '6': 33,
        '7': 31,
        '0': 0
    }
    if switcher.get(argumento, True):
        print("Escolha um opção Valida")
        escolhe_estado(input())
    return switcher.get(argumento)


def imprime_opcoes_estados():
    print('\n' * 50)
    print('*************** ESCOLHA UM ESTADO ***************')
    print('* <1> Paraná                                    *')
    print('* <2> Rio Grande do Sul                         *')
    print('* <3> Santa Catarina                            *')
    print('* <4> São Paulo                                 *')
    print('* <5> Espírito Santo                            *')
    print('* <6> Rio de Janeiro                            *')
    print('* <7> Minas Gerais                              *')
    print('* <0> Gerar Grafico                             *')
    print('*************************************************')


def sigla_estado_to_nome(argumento):
    switcher = {
        41: 'Paraná',
        43: 'Rio Grande do Sul',
        42: 'Santa Catarina',
        35: 'São Paulo',
        32: 'Espirito Santo',
        33: 'Rio de Janeiro',
        31: 'Minas Gerais'
    }
    return switcher.get(argumento, "Opção Inválida")





# def autolabel(rects, ax):
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')
