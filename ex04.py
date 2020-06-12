import numpy as np

while True:
    m = int(input("Digite o número de Linhas: "))
    n = int(input("Digite o números de Colunas: "))
    matrizM = np.zeros([m, n], dtype=float)
    print(matrizM)
    for i in range(m):
        for j in range(n):
            matrizM[i, j] = float(input(f"Digite o elemeto:[{i},{j}]  "))

    print(matrizM)
    k = int(input("Digite o números da constante K: "))
    matrizN = np.zeros([m, n], dtype=float)
    for i in range(m):
        for j in range(n):
            matrizN[i,j] = matrizM.sum(axis=0) + k
    print(matrizN)