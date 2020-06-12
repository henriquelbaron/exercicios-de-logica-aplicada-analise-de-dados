def mdc(x, y):
    if y == 0:
        resultado = x
    else:
        resultado = mdc(y, x % y)
    return resultado


def calcula_mdc(a, b):
    z = []
    for i in range(len(a)):
        z.append(mdc(a[i], b[i]))
    return z


A = [40, 24, 36, 42, 50]
B = [64, 36, 30, 28, 60]
C = calcula_mdc(A, B)
for i in range(len(C)):
    print('O mdc entre {} e {} é {}'.format(A[i], B[i], C[i]))
