import math
import numpy as np

def lerArquivo(nome):
    arquivo = open(nome, "r")
    matriz = []
    matrizA = []
    matrizB = []
    matrizC = []
    matrizD = []


    tags = ['*A','*B','*C','*D']
    
    for linha in arquivo:
        linha = linha.replace('\n',"")

        if(len(linha) > 0):
            matriz.append(linha.split())    

    contador = 0
    for i in (matriz):
        if i[0][0] == "*":
            contador += 1
        
        elif (contador == 1 ):
            matrizA.append(i)     

        elif (contador == 2):
            matrizB.append(i)

        elif (contador == 3):
            matrizC.append(i)

        elif (contador == 4):
            matrizD.append(i)
    print()
    print(matrizB)
    arquivo.close()
    return matriz
    
def comprimento(xa, ya, xb, yb):
	return math.sqr(math.pow(xa - xb, 2) + math.pow(xa - xb, 2) )
  
def cos(ya, xa, yb, xb, l):
    if (ya == yb):
        return 1
    elif (xa == xb):
        return 0
    else:
        return abs(yb - ya)/(l)

def sin(ya, xa, yb, xb, l):
    if (ya == yb):
        return 0
    elif (xa == xb):
        return 1
    else:
        return abs(xb - xa)/l

def area(base, altura):
    return base * altura

def matrixRigidez(k, s, c):
	return k *[[c**2 , c*s , -c**2, -c*s ],
              [c*s  , s**2 , -c*s , -s**2 ],
              [-c**2, -c*s , c**2 , c*s   ],
              [-c*s , -s**2, c*s  , s**2 ]]

def matrizGlobal(matrixA, matrixB, liberdade):
    for i in liberdade:
        for j in liberdade:
            matrizA[i][j] += matrixB[i][j]
    return matrizA
    
def main():
    arquivo = lerArquivo("entrada.txt")

main()

def matrixRestructure(matrix,graus):

    matriz = np.array(matrix)

    for i in graus:
        
        if i[1] == 1:
           matriz = np.delete(matriz,(i[0])-1,0)
        else:
             matriz = np.delete(matriz,(i[0])-1,1)

    return matriz


