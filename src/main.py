from math import *
import numpy as np

class ArquivoTXT():

    def __init__(self):
        self.matrizCordenadas    = []
        self.matrizElementos     = []
        self.matrizIndices       = []
        self.matrizMateriais     = []
        self.matrizPropriedades  = []
        self.matrizBcnodes       = []
        self.matrizLoads         = []
        self.quatidadeElementos = 0
        self.lerArquivo("entrada.txt")
        
    def lerArquivo(self, nome):
        arquivo = open(nome, "r")
        matriz = []
        tags = ["*COORDINATES","*ELEMENT_GROUPS","*INCIDENCES","*MATERIALS",
                "*GEOMETRIC_PROPERTIES","*BCNODES", "*LOADS"]
        
        for linha in arquivo:
            linha = linha.replace('\n',"")
            linha = linha.replace("BAR","")
        
            if(len(linha) > 0):
                matriz.append(linha.split())    

        flag = ""
        for i in (matriz):
            
            if i[0][0] == "*":
                flag = i[0]
            
            elif ( len(i) == 1): 
                    if(flag == "*ELEMENT_GROUPS"):
                        self.quantidadeElementos = i[0]
            
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
        self.liberdade = []
        self.main()
             
    def main(self):
        self.getCordenadas()
        self.comprimento()
        self.cos()
        self.sin()
        self.area()
        self.getMatrizRigidez()
        self.status()
        self.getLiberdade()

    def getCordenadas(self):
        self.coordenadas = [[0,0],[0,0]]
        
        self.coordenadas[0][0] = self.data.matrizCordenadas[int(self.incidencias[1] - 1)][1]
        self.coordenadas[0][1] = self.data.matrizCordenadas[int(self.incidencias[1] - 1)][2]
      
        self.coordenadas[1][0] = self.data.matrizCordenadas[int(self.incidencias[2] - 1)][1]
        self.coordenadas[1][1] = self.data.matrizCordenadas[int(self.incidencias[2] - 1)][2]
      
    def comprimento(self):
        self.comprimento = sqrt(pow(self.coordenadas[0][0] - self.coordenadas[1][0], 2) + pow(self.coordenadas[0][1] - self.coordenadas[1][1], 2))
        
    def cos(self):
        if(self.coordenadas[0][1] == self.coordenadas[1][1]):
            self.c =  1
        elif(self.coordenadas[0][0] == self.coordenadas[1][0]):
            self.c =  0
        else:
            self.c = abs(self.coordenadas[0][1] - self.coordenadas[1][1])/(self.comprimento)

    def sin(self):
        if(self.coordenadas[0][1] == self.coordenadas[1][1]):
            self.s =  0
        elif(self.coordenadas[0][0] == self.coordenadas[1][0]):
            self.s =  1
        else:
            self.s = abs(self.coordenadas[0][0] - self.coordenadas[1][0])/(self.comprimento)

    def area(self):
        self.area = self.propriedade[1]

   def getMatrixRigidez(self):
        k = int((self.material[0] * self.area) / self.comprimento) 
        matriz =    [[self.c**2 , self.c* self.s , -self.c**2, -self.c* self.s ],
                    [self.c* self.s  , self.s**2 , -self.c* self.s , -self.s**2 ],
                    [-self.c**2, -self.c* self.s , self.c**2 , self.c* self.s   ],
                    [-self.c* self.s , -self.s**2, self.c* self.s  , self.s**2 ]]

        
        self.matrizRigidez = []

        for e in matriz:
            self.matrizIntermediaria = []
            for i in e:
                self.matrizIntermediaria.append(k*i)
            self.matrizRigidez.append(self.matrizIntermediaria)
        
    def getLiberdade(self):
        for i in (self.incidencias[1:]):
            self.liberdade.append(i)
            self.liberdade.append(i + 1)

    
    def status(self):
        print("Elemento: ",self.numeroE)
        print("incidencias: ",self.incidencias)
        print("material: ",self.material)   
        print("Propriedade: ",self.propriedade)
        print("Comprimento: ",self.comprimento)
        print("cos :",self.c)
        print("sen :",self.s)
        print("Area:", self.area)
        print("matrizRigidez: ",self.matrizRigidez)
        print()


class CalculoGlobal():

    def __init__(self):
        self.data = ArquivoTXT()
        self.elemento = []
        self.main()
        
    def main(self):
        for i in range(1, int(self.data.quantidadeElementos) + 1):
            print("---------------",i)
            self.elemento.append(Elemento(i))
        self.matrizGlobal()

    def matrizGlobal(self):    
        s = (int(self.data.quantidadeElementos) * 2,int(self.data.quantidadeElementos) * 2)
        self.matrizGlobal = np.zeros(s)
        
        for obj in (self.elemento):
            contadorLinha = 0
            contadorColuna = 0
            for i in (obj.liberdade):
                for j in(obj.liberdade):
                    self.matrizGlobal[int(i) - 1][int(j) - 1] = obj.matrizRigidez[contadorLinha][contadorColuna] 
                contadorColuna += 1
            contadorLinha += 1 
        print(self.matrizGlobal)
        
    
    def matrizRestruturada(self):

CalculoGlobal()



