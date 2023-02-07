'''#ex1
matriz= []
for linha in range(3):
    matriz.append([])
    for coluna in range(3):
        matriz[linha].append(int(input (f"Digite o número de {linha+1}x{coluna+1}: ")))
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end="")
    print()
d = (matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[0][1] * matriz[1][2] * matriz[2][0] + matriz[0][2] * matriz[1][0] * matriz[2][1])
print(f'O determinante será o {d}')


#ex2
i = int (input("Digite o número de linhas: "))
j = int (input("Digite o número de colunas: ")) 
soma = 0
h=[]
matriz= []
for linha in range(0,i):
    matriz.append([])
    for coluna in range(0,j):
        matriz[linha].append(int(input ("Digite o número de {}x{}: ".format(linha+1, coluna+1))))
a = 0 
b = 0 
for linha in matriz:
    for coluna in matriz[a]: 
        if a == b:
            h.append(coluna)
        print ("\t {}".format(coluna), end = "")
        b +=1
    print() 
    a+=1
    b=0 
print ('{}'.format(h))


#ex4
import math
a = float(input('Informe a hipotenusa: '))
b = float(input('Informe o ângulo: '))
seno = math.sin(math.radians(b))
altura = seno * a
print(f'A altura do prédio tem {altura:.3f}m')'''


#ex3
'''vet = []

for i in range(30):
    vet.append(int(input('Informe números: ')))

def sub():
    for i in range(30):
        if (vet[i] >= 0):
            vet[i] = 1
        else:
            vet[i] = 0

sub()
print(vet)
    '''

'''#ex5
vet = []

for num in range(10):
    vet.append(int(input('Digite algum número: ')))
print(vet)
def test():
    print(set(vet))
    print(len(set(vet)))

test()'''

#ex6
set = {1,2,3,4}

print(type(set))
print(set)
set.add(2)
set.add(-12)
print('Adição', set)