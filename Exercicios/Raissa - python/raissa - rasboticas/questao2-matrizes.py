#Raissa Tainá Pordeus Ferreira
#Usando Numpy, crie duas matrizes A e B 3x3 onde os elementos de b serão os senos dos elementos de A.
import numpy as np


matriz_A = ([[10, 3, 4],
             [7, 0, 5],
             [3, 66, 9]])
matriz_B = ([[np.sin(10), np.sin(3), np.sin(4)],
             [np.sin(7), np.sin(0), np.sin(5)],
             [np.sin(3), np.sin(66), np.sin(9)]])

print('Sua matriz é: \n')
print(f'{matriz_A}\n')
print('Sua matriz de senos é: \n')
print(f'{matriz_B}\n')

#Fiz de outro jeito para treinar como pegar os valores nessa linguagem
#import numpy as np
#a = np.zeros((3,3), dtype=np.float64)

#print('Informe os valores de cada posição na direção de linha e dê enter\n')
#for i in range(0,3):
 # for j in range(0,3):
  #  a[i][j]=int(input())

#print(a)
#b = np.zeros((3,3), dtype=np.float64)

#for i in range(0,3):
 #   for j in range(0,3):
  #      b[i][j]=np.sin(a[i][j])

#print(b)