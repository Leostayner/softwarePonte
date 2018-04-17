from math import *
import numpy as np
from numpy.linalg import inv, det
import solver_gauss

class ArquivoTXT():

    def __init__(self):
        self.matrizCordenadas    = []
        self.matrizElementos     = []
        self.matrizIndices       = []
        self.matrizMateriais     = []
        self.matrizPropriedades  = []
        self.matrizBcnodes       = []
        self.matrizLoads         = []
        self.quantidadeNos = 0
        self.quantidadeforcas = 0
        self.quantidadeBCNodes = 0
        self.qunatidadeElementos = 0
        self.lerArquivo("entradaInterface.txt")
        
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
                    if(flag == "*COORDINATES"):
                        self.quantidadeNos = i[0]
                    
                    elif(flag == "*ELEMENT_GROUPS"):
                        self.quantidadeElementos = i[0]

                    elif(flag == "*LOADS"):
                        self.quantidadeforcas = i[0]

                    elif(flag == "*BCNODES"):
                        self.quantidadeBCNodes = i[0]
            
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
        self.getLiberdade()
        self.status()

    def getCordenadas(self):
        self.coordenadas = [[0,0],[0,0]]
        
        self.coordenadas[0][0] = self.data.matrizCordenadas[int(self.incidencias[1] - 1)][1]
        self.coordenadas[0][1] = self.data.matrizCordenadas[int(self.incidencias[1] - 1)][2]
      
        self.coordenadas[1][0] = self.data.matrizCordenadas[int(self.incidencias[2] - 1)][1]
        self.coordenadas[1][1] = self.data.matrizCordenadas[int(self.incidencias[2] - 1)][2]
      
    def comprimento(self):
        self.comprimento = sqrt(pow(self.coordenadas[0][0] - self.coordenadas[1][0], 2) + pow(self.coordenadas[0][1] - self.coordenadas[1][1], 2))
        
    def cos(self):
        if(self.coordenadas[1][0] > self.coordenadas[0][0]):
            signal =  1
        
        else:
            signal = -1

        if(self.coordenadas[0][1] == self.coordenadas[1][1]):
            self.c = signal
        
        elif(self.coordenadas[0][0] == self.coordenadas[1][0]):
            self.c =  0
        
        else:
            self.c = (self.coordenadas[1][0] - self.coordenadas[0][0])/(self.comprimento)

    def sin(self):
        
        if(self.coordenadas[1][1] > self.coordenadas[0][1]):
            signal =  1
        
        else:
            signal = -1
        
        if(self.coordenadas[0][1] == self.coordenadas[1][1]):
            self.s =  0
        
        elif(self.coordenadas[0][0] == self.coordenadas[1][0]):
            self.s =  signal
            
        else:
            self.s = (self.coordenadas[1][1] - self.coordenadas[0][1])/(self.comprimento)

    def area(self):
        self.area = self.propriedade[1]

    def getMatrizRigidez(self):
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
        
        self.matrizRigidez  = np.array(self.matrizRigidez) 
        
    def getLiberdade(self):
        for i in (self.incidencias[1:]):
                self.liberdade.append((i * 2) -1)
                self.liberdade.append(i * 2)
            
    
    def status(self):
        print("Elemento: ",self.numeroE)
        print("incidencias: ",self.incidencias)
        print("material: ",self.material)   
        print("Propriedade: ",self.propriedade)
        print("Comprimento: ",self.comprimento)
        print("Liberdade:", self.liberdade )
        print("cos :",self.c)
        print("sen :",self.s)
        print("Area:", self.area)
        print("MatrizRigidez \n {0} \n".format(self.matrizRigidez))






class CalculoGlobal():

    def __init__(self):
        self.data = ArquivoTXT()
        self.elemento = []
        self.main()
        
    def main(self):
        for i in range(1, int(self.data.quantidadeElementos) + 1):
            self.elemento.append(Elemento(i))
        
        self.numeroElemento = int(self.data.quantidadeElementos)
        self.matrizGlobal()
        self.vetorForca()
        self.matrizRestructure()
        self.matrizInversa()
        self.getReacaoApoio()
        self.getDeformacaoEspecfica()
        self.getTensao()
        self.status()

    def matrizGlobal(self):    
        s = (int(self.data.quantidadeNos) * 2,int(self.data.quantidadeNos) * 2)
        self.matrizGlobal = np.zeros(s)
        
        for obj in (self.elemento):
            contadorLinha = 0
            for i in (obj.liberdade):
                contadorColuna = 0
                for j in(obj.liberdade):
                    self.matrizGlobal[int(i) - 1][int(j) - 1] += obj.matrizRigidez[contadorLinha][contadorColuna]
                    contadorColuna += 1
                contadorLinha += 1 
        

    def vetorForca(self):
        s = (int(self.data.quantidadeNos) * 2, 1)
        self.vetorF = np.zeros(s)
        for i in range(int(self.data.quantidadeforcas)):
            
            if(self.data.matrizLoads[i][1] == 1.0): 
                indice = (int(self.data.matrizLoads[i][0]) * 2) - 2 
                self.vetorF[indice][0] =  self.data.matrizLoads[i][2]
            
            elif(self.data.matrizLoads[i][1] == 2.0):
                indice = (int(self.data.matrizLoads[i][0]) * 2 ) - 1
                self.vetorF[indice][0] =  self.data.matrizLoads[i][2]
        
    def matrizRestructure(self):
        self.matrizCortada = np.array(self.matrizGlobal)
        self.matrizFCortada = np.array(self.vetorF)
        self.graus = []
        contador = 0

        for i in range(int(self.data.quantidadeBCNodes)):
            if(self.data.matrizBcnodes[i][1] == 1.0):
                self.graus.append(int(self.data.matrizBcnodes[i][0] * 2) - 2)

            elif(self.data.matrizBcnodes[i][1] == 2.0):
                self.graus.append(int(self.data.matrizBcnodes[i][0] * 2) - 1)
    
        for i in self.graus:
            self.matrizCortada = np.delete(self.matrizCortada, i - contador, 0)
            self.matrizCortada = np.delete(self.matrizCortada, i - contador, 1)
            
            self.matrizFCortada = np.delete(self.matrizFCortada, i - contador, 0)
            
            contador += 1
       
    def matrizInversa(self):
        ite = 600
        tol =  0.000000001
        self.u,a,b = solver_gauss.metodos (ite, tol, self.matrizCortada, self.matrizFCortada, len(self.matrizFCortada))
        #dete = det(self.matrizCortada)
        #invC = inv(self.matrizCortada)
        #self.u = np.matmul(invC, self.matrizFCortada)
       
    
    def getReacaoApoio(self):
        s = (int(self.data.quantidadeNos) * 2)
        indice = (s,1)
        contador = 0
        self.matrizDeslocamento = np.zeros(indice)
       
       
        for i in (self.graus):
            self.matrizDeslocamento[i] = 1 
            
        for i in range(s):
            if(self.matrizDeslocamento[i] == 1):
                self.matrizDeslocamento[i] = 0
            
            elif(self.matrizDeslocamento[i] == 0):
                self.matrizDeslocamento[i] = self.u[contador]
                contador += 1
        
        self.reacaoApoio = np.matmul(self.matrizGlobal, self.matrizDeslocamento)
    

    def getDeformacaoEspecfica(self):
        self.deformacaoEspecifica = []
        indice= (4,1)
        
        for obj in(self.elemento):
            matrizSenCos = [-obj.c, -obj.s, obj.c, obj.s]
            matrizDeslocamentoEspecifico = np.zeros(indice)
            
            contador = 0
            for i in (obj.liberdade):
                matrizDeslocamentoEspecifico[contador] = self.matrizDeslocamento[int(i - 1)]     
                contador += 1
            
            for i in range(4):
                matrizSenCos[i] = 1/ obj.comprimento * matrizSenCos[i] 
  
            valor = np.matmul(matrizSenCos, matrizDeslocamentoEspecifico )
            self.deformacaoEspecifica.append(float(valor))
            
    def getTensao(self):
        self.tensaoEspecifica = []
        for i in range(int(self.numeroElemento)):
                tensao = self.elemento[i].material[0] * self.deformacaoEspecifica[i]
                self.tensaoEspecifica.append(tensao)
                

    def status(self):
        print("Global \n {0} \n".format(self.matrizGlobal))
        print("Forca \n {0} \n".format(self.vetorF))
        print("Global Cortada \n {0} \n".format(self.matrizCortada))
        print("Forca Cortada \n {0} \n".format(self.matrizFCortada))
        print("Deslocamento \n {0} \n".format(self.u))
        print("Deslocamento \n {0} \n".format(self.matrizDeslocamento))
        print("Reacao Apoio \n {0} \n".format(self.reacaoApoio))
        print("Deformacao Especifica \n {0} \n".format(self.deformacaoEspecifica))
        print("Tensao \n {0} \n".format(self.tensaoEspecifica))




class GerarTXT():

    def __init__(self):
        self.dadosGlobal = CalculoGlobal()
        self.data = ArquivoTXT()
        arq = open("saida.txt", 'w')
        
        arq.write("*DISPLACEMENTS \n")
        arq.write(str(self.data.quantidadeNos) + "\n") 
        
        for i in range(1, int(self.data.quantidadeNos) + 1):
            arq.write(str(i) + " ")
        
            for j in range(2):
                if(j == 0):
                    arq.write(str(float(self.dadosGlobal.matrizDeslocamento[i * 2 - 2])) + " ")
                
                elif(j == 1):
                    arq.write(str(float(self.dadosGlobal.matrizDeslocamento[i * 2 - 1])) + "\n")
        

        arq.write("\n*REACTION_FORCES \n")
        arq.write(str(self.data.quantidadeBCNodes) + "\n")   

        for i in range(int(self.data.quantidadeBCNodes)):
            arq.write( str(int(self.data.matrizBcnodes[i][0])) + " ")
  
            if(self.data.matrizBcnodes[i][1] == 1.0):
                arq.write("FX = ")
                indice = int(self.data.matrizBcnodes[i][0] * 2) - 2
                arq.write(str(float(self.dadosGlobal.reacaoApoio[indice])) + "\n")

            elif(self.data.matrizBcnodes[i][1] == 2.0):
                arq.write("FY = ")
                indice = int(self.data.matrizBcnodes[i][0] * 2) - 1
                arq.write(str(float(self.dadosGlobal.reacaoApoio[indice])) + "\n" )
    
        arq.write("\n*ELEMENT_STAINS \n")
        arq.write(str(self.dadosGlobal.numeroElemento) + "\n")   
        for i in range( self.dadosGlobal.numeroElemento):
            arq.write(str(i+1) + " ")
            arq.write(str(self.dadosGlobal.deformacaoEspecifica[i] ) + "\n" )


        arq.write("\n*ELEMENT_STRESSES \n")
        arq.write(str(self.dadosGlobal.numeroElemento) + "\n")
        for i in range( self.dadosGlobal.numeroElemento):
            arq.write(str(i+1) + " ")
            arq.write(str(self.dadosGlobal.tensaoEspecifica[i]) + "\n")
            
        arq.close()

#CalculoGlobal()
#GerarTXT()

def run():
    CalculoGlobal()
    GerarTXT()



