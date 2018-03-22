import math

def lerArquivo(nome):
    arquivo = open(nome, "r")
    valores = []

    for linha in arquivo:
        if(linha != '\n'):
          valores.append(linha)  

    arquivo.close()
    return valores
  
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
	return k *[[c**2 , c*s  , -c**2, -c*s ],
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
#    l = comprimento()
#    area = area()
#    m_els = null
#    k = (m_els * area)/ l
#    matrizG = matrizGlobal()
    print(arquivo)
main()





