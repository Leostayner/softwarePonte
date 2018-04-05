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
    def __init__(self, numeroE):
        self.data = ArquivoTXT()
        self.main(numeroE - 1)
    
    def main(self,numeroE):
        self.getIncidencia(numeroE)
        self.getCordenadas()
        self.comprimento()
        self.cos()
        self.sin()
    

    def getIncidencia(self, numeroE):
        self.incidencias = [0, 0]
        self.incidencias[0] = int(self.data.matrizIndices[numeroE][1])
        self.incidencias[1] = int(self.data.matrizIndices[numeroE][2])
        print("Incidencias: ", self.incidencias)
       
    def getCordenadas(self):
        self.coordenadas = [[0,0],[0,0]]
        for i in range(2):
            for j in range(2):
                self.coordenadas[i][j] = self.data.matrizCordenadas[self.incidencias[i]][self.incidencias[j]]
        print("Coordenadas: ", self.coordenadas)
      
    def comprimento(self):
        self.comprimento = sqrt(pow(self.coordenadas[0][0] - self.coordenadas[1][0], 2) + pow(self.coordenadas[0][1] - self.coordenadas[1][1], 2))
        print(self.comprimento)

    def cos(self):
        if(self.coordenadas[0][1] == self.coordenadas[1][1]):
            self.cos =  1
        elif(self.coordenadas[0][0] == self.coordenadas[1][0]):
            self.cos =  0
        else:
            self.cos = abs(self.coordenadas[0][1] - self.coordenadas[1][1])/(self.comprimento)
        print("cos :",self.cos)

    def sin(self):
        if(self.coordenadas[0][1] == self.coordenadas[1][1]):
            self.cos =  0
        elif(self.coordenadas[0][0] == self.coordenadas[1][0]):
            self.cos =  1
        else:
            self.cos = abs(self.coordenadas[0][0] - self.coordenadas[1][0])/(self.comprimento)
        print("sen :",self.cos)

#    def area(self):
    
#    def matrizGlobal(self):

#    def matrizRestruturada(self):



Elemento(1)


