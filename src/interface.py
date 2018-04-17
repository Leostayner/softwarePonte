import tkinter as tk
from PIL import ImageTk
from PIL import Image
import main


class Janela_Principal():
    
    def __init__(self):
        
        self.app_config = dict()
        self.app_config['width_button'] = 97
        self.app_config['height_button'] = 125

        self.app_config['max_height'] = 690
        self.app_config['max_width'] =  1000

        self.app_config['window_xpos'] = 100
        self.app_config['window_ypos'] = 100
        
        window_width  = self.app_config['max_width']
        window_height = self.app_config['max_height']

        self.window = tk.Tk()
        self.window.geometry("{}x{}+{}+{}".format(window_width, 
                                                  window_height, 
                                                  self.app_config['window_xpos'], 
                                                  self.app_config['window_ypos']))
        self.window.title("Análise de Treliças Planas")
        self.window.resizable(False, False)
    
        # Geometria da pagina
        self.window.rowconfigure(0, minsize = window_height)
        self.window.columnconfigure(0, minsize = window_height)
        
        # Menu Principal
        self.menu_principal = Menu_Principal(self)
    
        # Iniciar menu
        self.menu_principal.mostrar()

        
    def iniciar(self):
        self.window.mainloop()

class Menu_Principal():
    
    def __init__(self, janela_principal):
        self.matrizPontos = []
        self.elemento = []
        self.incidecias = []
        self.matrizIncidencias = []
        self.matrizPropriedades = []
        self.matrizBCNodes = []
        self.matrizLoad = []
        self.matrizMaterias = []
        self.conterElementos = 0
        self.conterPontos = 0
        self.conterBCNodes = 0
        self.conterLoads = 0
        self.conterInterno = 1
        
        self.janela_principal = janela_principal
        self.window1 = tk.Frame(self.janela_principal.window)
        self.window1.grid(row = 0, column = 0, sticky = "nsew")
        self.window1.configure(background = 'white')
        
        # Geometria da pagina        
        self.window1.rowconfigure(0, minsize = (self.janela_principal.app_config['max_height'] /20  ) )
        self.window1.rowconfigure(1, minsize = (self.janela_principal.app_config['max_height'] /20  ) - 4)
        self.window1.rowconfigure(2, minsize = (self.janela_principal.app_config['max_height'] /20  )- 4)
        self.window1.rowconfigure(3, minsize = (self.janela_principal.app_config['max_height'] /20  )- 4)
        self.window1.rowconfigure(4, minsize = (self.janela_principal.app_config['max_height'] /20  )- 4)
        self.window1.rowconfigure(5, minsize = (self.janela_principal.app_config['max_height'] /20  )- 4)
        self.window1.rowconfigure(6, minsize = (self.janela_principal.app_config['max_height'] /20  ))
        self.window1.rowconfigure(7, minsize = (self.janela_principal.app_config['max_height'] /20  ))
        self.window1.rowconfigure(8, minsize = (self.janela_principal.app_config['max_height'] /20  ))
        self.window1.rowconfigure(9, minsize = (self.janela_principal.app_config['max_height'] /20   ))
        self.window1.rowconfigure(10, minsize = (self.janela_principal.app_config['max_height'] /20   ))
        self.window1.rowconfigure(11, minsize = (self.janela_principal.app_config['max_height'] /20   ))
        self.window1.rowconfigure(12, minsize = (self.janela_principal.app_config['max_height'] /20   ))
        self.window1.rowconfigure(13, minsize = (self.janela_principal.app_config['max_height'] /20   ))
        self.window1.rowconfigure(14, minsize = (self.janela_principal.app_config['max_height'] /20   ))
        self.window1.rowconfigure(15, minsize = (self.janela_principal.app_config['max_height'] /20   ))
        self.window1.rowconfigure(16, minsize = (self.janela_principal.app_config['max_height'] /20   ))
        self.window1.rowconfigure(17, minsize = (self.janela_principal.app_config['max_height'] /20   ))
        self.window1.rowconfigure(18, minsize = (self.janela_principal.app_config['max_height'] /20   ))
        self.window1.rowconfigure(19, minsize = (self.janela_principal.app_config['max_height'] /20   ))


        self.window1.columnconfigure(0, minsize = (self.janela_principal.app_config['max_width'] / 1.5) )
        self.window1.columnconfigure(1, minsize = (self.janela_principal.app_config['max_width'] / 6) )
        self.window1.columnconfigure(2, minsize = (self.janela_principal.app_config['max_width'] / 6) )

        self.canvas = tk.Canvas(self.window1)
        self.canvas.configure(bg = "white", highlightthickness = 0)
        self.canvas.grid(row = 0, rowspan = 12, column = 0, sticky = "nsew")
        self.canvas.create_line(5, 430, 650, 430, width=5)
        self.canvas.create_line(650, 430, 650, 4, width=5)
        self.canvas.create_line(5, 5, 650, 5, width=5)
        self.canvas.create_line(5, 5, 5, 430, width=5)
        
        self.Legenda = ImageTk.PhotoImage(Image.open("./legenda.png"))
        self.Legenda_label = tk.Label(self.window1,image = self.Legenda, bg = "white")
        self.Legenda_label.grid(row = 14, rowspan = 1, column = 0, columnspan = 1, sticky = "nsew") 
        
        self.Logo = ImageTk.PhotoImage(Image.open("./imageLogo.png"))
        self.Logo_label = tk.Label(self.window1,image = self.Logo, height = 4, width = 30)
        self.Logo_label.grid(row = 0, column = 1, columnspan = 2, sticky = "nsew")        
        
        #Entry Pontos
        self.textPointx = tk.StringVar()
        self.pointx = tk.Entry(self.window1, textvariable = self.textPointx)        
        self.pointx.grid(row = 1, column = 1, sticky="ew")
      
        self.textPointy = tk.StringVar()
        self.pointy = tk.Entry(self.window1, textvariable = self.textPointy)        
        self.pointy.grid(row = 1, column = 2, sticky="ew")
      
        self.button_point = tk.Button(self.window1) 
        self.button_point.configure(text = "Adicionar Ponto", command = self.botao_point)       
        self.button_point.grid(row = 2, column = 1, columnspan = 2,sticky = "ew")
       
        #Lista de Pontos
        self.ListPoint = tk.Listbox(self.window1, height = 5)  
        self.ListPoint.grid(row = 3, column = 1,sticky = "ew")

        self.ListPoint2 = tk.Listbox(self.window1, height = 5)  
        self.ListPoint2.grid(row = 3, column = 2,sticky = "ew")
        
        #Label Elemento
        self.textElemento = tk.StringVar()
        self.labelElementos = tk.Label(self.window1)
        self.labelElementos.configure(textvariable = self.textElemento)
        self.labelElementos.grid(row = 4, column = 1, columnspan = 2, sticky = "sew")
        self.textElemento.set("Incidencias")

        #Incidencias Elemento
        self.selectpoint1 = tk.StringVar()
        self.pointSelect = tk.Entry(self.window1, textvariable = self.selectpoint1)
        self.pointSelect.grid(row = 5, column = 1,sticky = "ew")

        self.selectpoint2 = tk.StringVar()
        self.pointSelect2 = tk.Entry(self.window1, textvariable = self.selectpoint2)
        self.pointSelect2.grid(row = 5, column = 2,sticky = "ew")

        #Area
        self.labelArea = tk.Label(self.window1)
        self.labelArea.configure(text = "Área:")
        self.labelArea.grid(row = 6, column = 1, sticky = "ew")

        self.textArea = tk.StringVar()
        self.Area = tk.Entry(self.window1, textvariable = self.textArea)        
        self.Area.grid(row = 6, column = 2)




        #Material
        self.labelElasticidade = tk.Label(self.window1)
        self.labelElasticidade.configure(text = "M. Elasticidade:")
        self.labelElasticidade.grid(row = 7, column = 1, sticky = "ew")

        self.varElasticidade = tk.StringVar()
        self.entryElasticidade = tk.Entry(self.window1, background = "white", textvariable = self.varElasticidade)
        self.entryElasticidade.grid(row = 7, column = 2)

        
        self.labelTracao = tk.Label(self.window1)
        self.labelTracao.configure(text = "T.ADM Tração:")
        self.labelTracao.grid(row = 8, column = 1, sticky = "ew")

        self.varTracao = tk.StringVar()
        self.entryTracao = tk.Entry(self.window1, background = "white", textvariable = self.varTracao)
        self.entryTracao.grid(row = 8, column = 2)



        self.labelCompressao = tk.Label(self.window1)
        self.labelCompressao.configure(text = "T.ADM Compressão:")
        self.labelCompressao.grid(row = 9, column = 1, sticky = "ew")

        self.varCompressao = tk.StringVar()
        self.entryCompressao = tk.Entry(self.window1, background = "white",textvariable = self.varCompressao)
        self.entryCompressao.grid(row = 9, column = 2)

        

        #Criar Elemento
        self.button_Element = tk.Button(self.window1)        
        self.button_Element.configure(text = "Criar Elemento", command = self.criarElemento)
        self.button_Element.grid(row = 10, column = 1, columnspan = 2, sticky = "sew")

        
        #Pinagem
       
        self.labelBCNode = tk.Label(self.window1)
        self.labelBCNode.configure(text = "Nó:")
        self.labelBCNode.grid(row = 11, column = 1,sticky = "ew")

        self.varBCnode = tk.StringVar()
        self.bcNode = tk.Entry(self.window1, textvariable = self.varBCnode)
        self.bcNode.grid(row = 11, column = 2)
  
        self.button_bcFx = tk.Button(self.window1, text = 'Travar Fx')
        self.button_bcFx.grid(row = 12, column = 1)
        self.button_bcFx.configure(command = self.travarbcFx)

        self.button_bcFy = tk.Button(self.window1, text = 'Travar Fy')
        self.button_bcFy.grid(row = 12, column = 2)
        self.button_bcFy.configure(command = self.travarbcFy)

        self.button_travar = tk.Button(self.window1, text = 'Travar')
        self.button_travar.grid(row = 13, column = 1,columnspan = 2,sticky = "ew")
        self.button_travar.configure(command = self.travar)



        #Loads

        self.Label_ElementoForca = tk.Label(self.window1)
        self.Label_ElementoForca.configure(text = "Nó:")
        self.Label_ElementoForca.grid(row = 14, column = 1,sticky = "ew")
    
        self.elementoForca = tk.StringVar()
        self.entryElementoForca = tk.Entry(self.window1, textvariable = self.elementoForca)
        self.entryElementoForca.grid(row = 14, column = 2)


        self.Label_SentidoForca = tk.Label(self.window1)
        self.Label_SentidoForca.configure(text = "Sentido")
        self.Label_SentidoForca.grid(row = 15, column = 1,sticky = "ew")

        self.sentidoForca = tk.StringVar()
        self.entrySentidoForca = tk.Entry(self.window1, textvariable = self.sentidoForca)
        self.entrySentidoForca.grid(row = 15, column = 2)


        self.Label_Forca = tk.Label(self.window1)
        self.Label_Forca.configure(text = "Força:")
        self.Label_Forca.grid(row = 16, column = 1,sticky = "ew")

        self.Forca = tk.StringVar()
        self.entryForca = tk.Entry(self.window1, textvariable = self.Forca )
        self.entryForca.grid(row = 16, column = 2)


        self.button_Load = tk.Button(self.window1)        
        self.button_Load.configure(text = "Adicionar Força", command = self.load)
        self.button_Load.grid(row = 17, column = 1, columnspan = 2, sticky = "ew")



        self.button_Analisar = tk.Button(self.window1)        
        self.button_Analisar.configure(text = "Analisar", command = self.criarTXT)
        self.button_Analisar.grid(row = 16, column = 0)

    def mostrar(self):
        self.window1.tkraise()

    def travarbcFx(self):
        self.trava = 1
        self.button_bcFx.config(state="disable")
        self.button_bcFy.config(state="normal")

    def travarbcFy(self):
        self.trava = 2
        self.button_bcFx.config(state="normal")
        self.button_bcFy.config(state="disable")

    def travar(self):
        self.conterBCNodes += 1
        vetorTrava = [self.varBCnode.get(), str(self.trava)]
        self.matrizBCNodes.append(vetorTrava)
        
        lista_travas = []
        
        self.x0 = float(self.matrizPontos[int(self.varBCnode.get())-1][1])*400 + 100
        self.y0 = -float(self.matrizPontos[int(self.varBCnode.get())-1][2])*400 + 400

        for i in range(len(self.matrizBCNodes)):
            if self.matrizBCNodes[i][0] == self.varBCnode.get():
                lista_travas.append(self.matrizBCNodes[i][1])
            
        if len(lista_travas) > 1:
            self.canvas.create_oval(self.x0, self.y0, self.x0+5.0, self.y0+5.0, width=3, outline='#9933ff', fill='#9933ff')
        elif lista_travas[0] == '1':
            self.canvas.create_oval(self.x0, self.y0, self.x0+5.0, self.y0+5.0, width=3, outline='#ff0000', fill='#ff0000')
        elif lista_travas[0] == '2':
            self.canvas.create_oval(self.x0, self.y0, self.x0+5.0, self.y0+5.0, width=3, outline='#00ccff', fill='#00ccff')
        
        
        self.bcNode.delete(0,"end")
        self.button_bcFx.config(state="normal")
        self.button_bcFy.config(state="normal")

    def load(self):
        self.conterLoads += 1
        vetorLoad = [self.elementoForca.get(), self.sentidoForca.get(), self.Forca.get()]
        self.matrizLoad.append(vetorLoad)

        self.entryElementoForca.delete(0,"end")
        self.entryForca.delete(0,"end")
        self.entrySentidoForca.delete(0,"end")

    def botao_point(self):
        print(len(self.textPointx.get()))
        
        if((len(self.textPointx.get()) == 3 ) and (len(self.textPointx.get()) == 3)):
            self.conterPontos += 1
            
            self.x0 = float(self.textPointx.get())*400 + 100 
            self.y0 = -float(self.textPointy.get())*400 + 400
            self.canvas.create_oval(self.x0, self.y0, self.x0+5.0, self.y0+5.0, width=3, fill='black')
            
            self.ListPoint.insert(self.conterPontos,str(self.conterPontos) + "  " + self.textPointx.get() + "  " + self.textPointy.get())
        
            self.vetorPontos = [self.conterPontos, self.textPointx.get(), self.textPointy.get()]
            self.matrizPontos.append(self.vetorPontos)
        
        self.pointx.delete(0, 'end')
        self.pointy.delete(0, 'end')

    
    def criarElemento(self):
        self.conterElementos += 1
        
        self.x0 = float(self.matrizPontos[int(self.selectpoint1.get())-1][1])*400 + 102
        self.y0 = -float(self.matrizPontos[int(self.selectpoint1.get())-1][2])*400 + 402
        self.x1 = float(self.matrizPontos[int(self.selectpoint2.get())-1][1])*400 + 102
        self.y1 = -float(self.matrizPontos[int(self.selectpoint2.get())-1][2])*400 + 402
        self.canvas.create_line(self.x0, self.y0, self.x1, self.y1, width=2,fill='black')

        vetorIncidencias = [self.conterElementos, self.selectpoint1.get(), self.selectpoint2.get()]
        self.matrizIncidencias.append(vetorIncidencias)
    

        self.matrizPropriedades.append(self.textArea.get())

        vetorMateriais = [self.varElasticidade.get(),self.varTracao.get(),self.varCompressao.get()]
        self.matrizMaterias.append(vetorMateriais)


        self.ListPoint2.insert( self.conterInterno ,"Elemento" +  str(self.conterElementos) + ":  (" + self.selectpoint2.get() + "  " + self.selectpoint2.get() + ")")
        self.conterInterno+=1
        self.ListPoint2.insert( self.conterInterno,"Area: " + self.textArea.get())
        self.conterInterno+=1
        self.ListPoint2.insert( self.conterInterno,"M.E: " +  self.varElasticidade.get())
        self.conterInterno+=1
        self.ListPoint2.insert( self.conterInterno,"T.A: " +  self.varTracao.get())
        self.conterInterno+=1
        self.ListPoint2.insert( self.conterInterno,"C.A: " +  self.varCompressao.get())
        self.conterInterno+=1
        self.ListPoint2.insert( self.conterInterno," ")
        self.conterInterno+=1



        self.Area.delete(0, 'end')

        self.entryElasticidade.delete(0,"end")
        self.entryTracao.delete(0,"end")
        self.entryCompressao.delete(0,"end")
        
        self.pointSelect.delete(0, 'end')
        self.pointSelect2.delete(0, 'end')

    def criarTXT(self):
        
        print(self.matrizPontos)
        arq = open("entradaInterface.txt", 'w')

        arq.write("*COORDINATES\n")
        arq.write(str(self.conterPontos) + "\n")
        for i in range(self.conterPontos):
            arq.write(str(i + 1) + " ")
            arq.write(str(self.matrizPontos[i][1]) + " ")
            arq.write(str(self.matrizPontos[i][2]) + "\n")
    
        arq.write("\n*ELEMENT_GROUPS\n")
        arq.write(str(self.conterElementos) + "\n")
        for i in range(self.conterElementos):
            arq.write(str(i + 1) + " ")
            arq.write("1 ")
            arq.write("BAR\n")
            
        arq.write("\n*INCIDENCES\n")
        arq.write(str(self.conterElementos) + "\n")
        for i in range(self.conterElementos):
            arq.write(str(i + 1) + " ")
            arq.write(str(self.matrizIncidencias[i][1]) + " ")
            arq.write(str(self.matrizIncidencias[i][2]) + "\n")
            
        
        arq.write("\n*MATERIALS\n")
        arq.write(str(self.conterElementos) + "\n")
        for i in range(self.conterElementos):
            arq.write(str(self.matrizMaterias[i][0]) + " ")
            arq.write(str(self.matrizMaterias[i][1]) + " ")
            arq.write(str(self.matrizMaterias[i][2]) + "\n")


        arq.write("\n*GEOMETRIC_PROPERTIES\n")
        arq.write(str(self.conterElementos) + "\n")
        for i in range(self.conterElementos):
            arq.write(str(i + 1) + " ")
            arq.write(str(self.matrizPropriedades[i]) + "\n")
        
        arq.write("\n*BCNODES\n")
        arq.write(str(self.conterBCNodes) + "\n")
        for i in range(self.conterBCNodes):
            arq.write(str(self.matrizBCNodes[i][0]) + " ")
            arq.write(str(self.matrizBCNodes[i][1]) + "\n")
    
        arq.write("\n*LOADS\n")
        arq.write(str(self.conterLoads) + "\n")
        for i in range(self.conterLoads):
            arq.write(str(self.matrizLoad[i][0]) + " ")
            arq.write(str(self.matrizLoad[i][1]) + " ")
            arq.write(str(self.matrizLoad[i][2]) + "\n")
        
        arq.close()
        
        main.run()

app = Janela_Principal()
app.iniciar()