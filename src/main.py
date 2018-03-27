import math
import numpy as np

def lerArquivo(nome):
    arquivo = open(nome, "r")
       

    matrizA = False
    matrizB = False

    matrizNo = []
    matrizE = []

    tags = ["*A","*B","*C","*D"]
    
    for linha in arquivo:
        linha = linha.replace('\n',"")
        
        if(linha == tags[0]):
            matrizA = True    

        elif(linha == tags[1]):
            matrizB = True
            matrizA = False
 
        elif(matrizA == True ) and (len(linha) > 1):
            if(linha[0] != '*'):
                matrizNo.append(linha.split())
        elif(matrizB == True ) and (len(linha) > 1):
            if(linha[0] != '*'):
                matrizE.append(linha.split())             
    
    arquivo.close()
    return matrizNo, matrizE
  
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
    arquivo, arquivo2 = lerArquivo("entrada.txt")
    print("MatrizA: {0} \n").format(arquivo)
    print("MatrizB: {0} \n" ).format(arquivo2)
main()

def matrixRestructure(matrix,graus):

    matriz = np.array(matrix)

    for i in graus:
        
        if i[1] == 1:
           matriz = np.delete(matriz,(i[0])-1,0)
        else:
             matriz = np.delete(matriz,(i[0])-1,1)

    return matriz


