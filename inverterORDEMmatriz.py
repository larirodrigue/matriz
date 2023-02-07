import random
mat = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        num = int(input('Digite algum número: '))
        mat[i][j] = num
print(mat)

mat1 = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        num = random.randint(0,9)
        mat1[i][j] = num
print(mat1)