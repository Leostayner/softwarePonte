from math import *

class ArquivoTXT():

    def __init__(self):
        self.matrizCordenadas    = []
        self.matrizElementos     = []
        self.matrizIndices       = []
        self.matrizMateriais     = []
        self.matrizPropriedades  = []
        self.matrizBcnodes       = []
        self.matrizLoads         = []
        self.lerArquivo("entrada.txt")

        
    def lerArquivo(self, nome):
        arquivo = open(nome, "r")
        matriz = []
        tags = ["*COORDINATES","*ELEMENT_GROUPS","*INCIDENCES","*MATERIALS",
                "*GEOMETRIC_PROPERTIES","*BCNODES", "*LOADS"]
        
        for linha in arquivo:
            linha = linha.replace('\n',"")
            linha = linha.replace("BAR","")

            if(len(linha) > 1):
                matriz.append(linha.split())    

        flag = ""
        for i in (matriz):
            
            if i[0][0] == "*":
                flag = i[0]
            
            else:
                for j in range(len(i)):
                    i[j] = float(i[j])

                if (flag == "*COORDINATES" ):
                    self.matrizCordenadas.append(i)     

                elif (flag == "*ELEMENT_GROUPS"):
                    self.matrizElementos .append(i)

                elif (flag == "*INCIDENCES"):
                    self.matrizIndices.append(i)

                elif (flag == "*MATERIALS"):
                    self.matrizMateriais.append(i)

                elif (flag == "*GEOMETRIC_PROPERTIES"):
                    self.matrizPropriedades.append(i)

                elif (flag == "*BCNODES"):
                    self.matrizBcnodes.append(i)

                elif (flag == "*LOADS"):
                    self.matrizLoads.append(i)
        arquivo.close()


class Elemento():
    def __init__(self, numeroElemento):
        self.numeroE = numeroElemento - 1  
        self.data = ArquivoTXT()

        self.incidencias   = self.data.matrizIndices[self.numeroE]
        self.material      = self.data.matrizMateriais[self.numeroE]
        self.propriedade   = self.data.matrizPropriedades[self.numeroE]
        print(self.propriedade)
        self.main()
             
    def main(self):
        self.getCordenadas()
        self.comprimento()
        self.cos()
        self.sin()
        self.area()
        self.getMatrixRigidez()
       
    def getCordenadas(self):
        self.coordenadas = [[0,0],[0,0]]
        
        self.coordenadas[0][0] = self.data.matrizCordenadas[int(self.incidencias[1] - 1)][1]
        self.coordenadas[0][1] = self.data.matrizCordenadas[int(self.incidencias[1] - 1)][2]
      
        self.coordenadas[1][0] = self.data.matrizCordenadas[int(self.incidencias[2] - 1)][1]
        self.coordenadas[1][1] = self.data.matrizCordenadas[int(self.incidencias[2] - 1)][2]
      
    def comprimento(self):
        self.comprimento = sqrt(pow(self.coordenadas[0][0] - self.coordenadas[1][0], 2) + pow(self.coordenadas[0][1] - self.coordenadas[1][1], 2))
        print(self.comprimento)

    def cos(self):
        if(self.coordenadas[0][1] == self.coordenadas[1][1]):
            self.c =  1
        elif(self.coordenadas[0][0] == self.coordenadas[1][0]):
            self.c =  0
        else:
            self.c = abs(self.coordenadas[0][1] - self.coordenadas[1][1])/(self.comprimento)
        print("cos :",self.c)

    def sin(self):
        if(self.coordenadas[0][1] == self.coordenadas[1][1]):
            self.s =  0
        elif(self.coordenadas[0][0] == self.coordenadas[1][0]):
            self.s =  1
        else:
            self.s = abs(self.coordenadas[0][0] - self.coordenadas[1][0])/(self.comprimento)
        print("sen :",self.s)

    def area(self):
        self.area = self.propriedade[self.numeroE + 1]
        print("Area:", self.area)

    def getMatrixRigidez(self):
        print(self.material[0])
        k = int((self.material[0] * self.area) / self.comprimento) 
        print(k)
        matriz =    [[self.c**2 , self.c* self.s , -self.c**2, -self.c* self.s ],
                    [self.c* self.s  , self.s**2 , -self.c* self.s , -self.s**2 ],
                    [-self.c**2, -self.c* self.s , self.c**2 , self.c* self.s   ],
                    [-self.c* self.s , -self.s**2, self.c* self.s  , self.s**2 ]]

        
        self.matrixRigidez = []

        for e in matriz:
            self.matrixIntermediaria = []
            for i in e:
                self.matrixIntermediaria.append(k*i)
            self.matrixRigidez.append(self.matrixIntermediaria)
            
        
        print(self.matrixRigidez)
        
        
Elemento(1)


#    def matrizRestruturada(self):










