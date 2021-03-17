#Raissa Tainá Pordeus Ferreira
#Usando Numpy, crie duas matrizes 4x4 e realize as seguintes operações:

#Soma
#Subtração
#Multiplicação
#Divisão
#Produto entre as duas matrizes
#Concatenação 
import numpy as np

a = np.zeros((4,4), dtype=np.float64) #criando uma matriz de zeros de ordem 4 para preencher com os valores informados

print('Este programa faz calculos basicos com matrizes. \n')
for i in range(0,4):#preenchendo a linha da matriz
  for j in range(0,4):#preenchendo a coluna
    a[i][j]=int(input(f'Informe o valor da posicao da primeira matriz [{i}, {j}]'))

print(a)
b = np.zeros((4,4), dtype=np.float64)#criando a matriz b na mesma logica da A


for i in range(0,4):#pegando as linhas
  for j in range(0,4):#peando as colunas
    b[i][j]=int(input(f'Informe o valor da posicao da segunda matriz [{i}, {j}]'))

print(b)
#fazendo os calculos
soma = a + b
print('Soma da matriz: \n', + soma)

subtracao = a - b
print('Subtracao da matriz: \n'
, + subtracao)

divisao = a / b
print('Divisao da matriz: \n', + divisao)

produto = a * b
print(('Produto da matriz: \n', + produto))

produtodamatriz=a.dot(b)
print('Produto de matrizes \n: ', + produtodamatriz)

concatenacao= np.concatenate((a,b), axis=0)
print('Concatenacao \n: ', +concatenacao)