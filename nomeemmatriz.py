mat = [[0 for i in range(2)] for j in range(2)]
for i in range(2):
    for j in range(2):
        name = str(input('Digite seu nome:'))
        mat[i][j] = name

for l in range(2):
    for c in range(2):
        print(f'{mat[l][c]:^10}', end=' ')
    print()