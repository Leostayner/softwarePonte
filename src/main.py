import math
from numpy.linalg import inv
import numpy as np

def lerArquivo(nome):
    arquivo = open(nome, "r")
    tags = ["*COORDINATES\n" ,"*ELEMENT_GROUPS\n", "*INCIDENCES\n",
            "*MATERIALS\n", "*GEOMETRIC_PROPERTIES\n", "*BCNODES\n", "*LOADS\n"]
    valores =[]

    n = 0
    for e in tags:
        contador = 0
        print("oooi")
        for linha in arquivo:
            if(e == linha):
                if e=="*INCIDENCES":
                    contador+=2
                contador+=1
                print("primeiro if")
            
            elif contador == 1:
                n = int(linha)
                contador += 1
                print("segundo if %d", n)

            elif contador<=(n+1) and linha !='\n':  
                print("terceiro if")          
                valores.append(linha.split())
                contador+=1
            else:
                pass
  

    arquivo.close()
    return valores
  
def comprimento(xa, ya, xb, yb):
	return math.sqrt(math.pow(xa - xb, 2) + math.pow(xa - xb, 2) )
  
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

def matrizRigidez(k, s, c):
	return k *[[c**2 , c*s  , -c**2, -c*s ],
              [c*s  , s**2 , -c*s , -s**2 ],
              [-c**2, -c*s , c**2 , c*s   ],
              [-c*s , -s**2, c*s  , s**2 ]]

def matrizGlobal(matrizA, matrizB, liberdade):
    for i in liberdade:
        for j in liberdade:
            matrizA[i][j] += matrizB[i][j]
    return matrizA
    
def cortaMatriz(no, matrizG):
    n = len(no)
    matrizC = [t-n][t-n]

def deslocamento (matrizC, forca):
    invC = inv(matrizC)
    deslocamento = np.matmul(forca, invC)
    

    

def main():
    arquivo = lerArquivo("entrada.txt")
#    l = comprimento()
#    area = area()
#    m_els = null
#    k = (m_els * area)/ l
#    matrizG = matrizGlobal()
    print(arquivo)
main()





