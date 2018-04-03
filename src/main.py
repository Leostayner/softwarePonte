import math
import numpy as np

class Ponte():

    def __init__(self):
        self.matrizCordenadas    = []
        self.matrizElementos     = []
        self.matrizIndices       = []
        self.matrizMateriais     = []
        self.matrizPropriedades  = []
        self.matrizBcnodes       = []
        self.matrizLoads         = []
        
    def main(self):    
        self.lerArquivo("entrada.txt")
        comprimento = self.comprimento(1)
        print(comprimento)        

    def lerArquivo(self, nome):
        arquivo = open(nome, "r")
        matriz = []
        tags = ['*COORDINATES','*ELEMENT_GROUPS','*INCIDENCES','*MATERIALS',
                '*GEOMETRIC_PROPERTIES','*BCNODES', '*LOADS']
        
        for linha in arquivo:
            linha = linha.replace('\n',"")

            if(len(linha) > 0):
                matriz.append(linha.split())    

        flag = ""
        for i in (matriz):
            if i[0][0] == "*":
                flag = i[0]
            
            elif (flag == '*COORDINATES' ):
                self.matrizCordenadas.append(i)     

            elif (flag == '*ELEMENT_GROUPS'):
                self.matrizElementos .append(i)

            elif (flag == '*INCIDENCES'):
                self.matrizIndices.append(i)

            elif (flag == '*MATERIALS'):
                self.matrizMateriais.append(i)
    
            elif (flag == '*GEOMETRIC_PROPERTIES'):
                self.matrizPropriedades.append(i)

            elif (flag == '*BCNODES'):
                self.matrizBcnodes.append(i)

            elif (flag == '*LOADS'):
                self.matrizLoads.append(i)
        arquivo.close()


    def comprimento(self, elemento):
        xa = self.matrizCordenadas[self.matrizIndices[elemento - 1][1]][1])
        yb = self.matrizCordenadas[self.matrizIndices[elemento - 1][1]][2])
        xb = self.matrizCordenadas[self.matrizIndices[elemento - 1][2]][1])
        yb = self.matrizCordenadas[self.matrizIndices[elemento - 1][2]][2])
        return math.sqr(math.pow(xa - xb, 2) + math.pow(xa - xb, 2)

'''      
def comprimento(self):


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
    
def matrixRestructure(matrix,graus):

    matriz = np.array(matrix)

    for i in graus:
        
        if i[1] == 1:
           matriz = np.delete(matriz,(i[0])-1,0)
        else:
             matriz = np.delete(matriz,(i[0])-1,1)

    return matriz

'''
Ponte().main()

