import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

from numpy.lib.function_base import append
import SimuladorFifo
import SimuladorNur
import SimuladorMru
import SimuladorSegundaChance
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def MetodoFIFO():
    global listFramesFifo,listAcertosFifo

    if(textoMetodo==[]):
        return
    #Peraparação  
    minFrameCount, maxFrameCount=Entrada1,Entrada2
    listFramesFifo= [x for x in range(minFrameCount, maxFrameCount + 1)]#Lista de Frames
    Referencia=''.join(str(item)for item in textoMetodo) #Tornar uma lista em String
    
    #O Metodo
    listAcertosFifo=SimuladorFifo.FIFO(Referencia,minFrameCount-1, maxFrameCount)
    
    #A Tabela
    if(textoAcertosFIFO==[]):
        textoAcertosFIFO.extend(listAcertosFifo)
    else:
        textoAcertosFIFO.clear()
        textoAcertosFIFO.extend(listAcertosFifo)
    tabela()

    #O grafico
    PlotarGrafico()
    

def MetodoNUR():
    global listFramesNUR,listAcertosNUR

    if(textoMetodo==[]):
        return
    #Peraparação
    pageReferenceDescription=''.join(str(item)for item in textoMetodo) #Tornar uma lista em String
    minFrameCount, maxFrameCount = Entrada1,Entrada2
    listFrames = [x for x in range(minFrameCount, maxFrameCount + 1)]#Lista de Frames
    listAcertos = []

    #O Metodo
    resetInterval = ResetInterval
    for i in range(minFrameCount, maxFrameCount + 1):
        listAcertos.append(SimuladorNur.nur(pageReferenceDescription, i, resetInterval))

    #A Tabela
    if(textoAcertosNUR==[]):
        textoAcertosNUR.extend(listAcertos)
    else:
        textoAcertosNUR.clear()
        textoAcertosNUR.extend(listAcertos)
    tabela()
    #O grafico
    listFramesNUR,listAcertosNUR=listFrames, listAcertos
    PlotarGrafico()


def MetodoSegundaChance():
    global listFramesSegundaChance,listAcertosSegundaChance
    
    if(textoMetodo==[]):
        return

    #Peraparação  
    minFrameCount, maxFrameCount=Entrada1,Entrada2
    listFramesSegundaChance= [x for x in range(minFrameCount, maxFrameCount + 1)]#Lista de Frames
    Referencia=''.join(str(item)for item in textoMetodo) #Tornar uma lista em String
    listAcertos=[]
    #O Metodo

    listAcertosSegundaChance=SimuladorSegundaChance.segunda_chance(Referencia, Entrada1,Entrada2)

    #A Tabela
    if(textoAcertosSegC==[]):
        textoAcertosSegC.extend(listAcertosSegundaChance)
    else:
        textoAcertosSegC.clear()
        textoAcertosSegC.extend(listAcertosSegundaChance)
    tabela()
    # O grafico
    PlotarGrafico()

    return
    # SimuladorSegundaChance.SegundaChance(textoMetodo[0],int(E1.get()))


def MetodoMRU():
    global listFramesMRU,listAcertosMRU

    if(textoMetodo==[]):
        return
    #Peraparação
    pageReferenceDescription=''.join(str(item)for item in textoMetodo) #Tornar uma lista em String
    minFrameCount, maxFrameCount = Entrada1,Entrada2
    listFrames = [x for x in range(minFrameCount, maxFrameCount + 1)]#Lista de Frames
    listAcertos = []

    #O Metodo
    for i in range(minFrameCount, maxFrameCount + 1):
        listAcertos.append(SimuladorMru.mru(pageReferenceDescription, i))

    #A Tabela
    if(textoAcertosMRU==[]):
        textoAcertosMRU.extend(listAcertos)
    else:
        textoAcertosMRU.clear()
        textoAcertosMRU.extend(listAcertos)
    tabela()
    #O grafico
    listFramesMRU,listAcertosMRU=listFrames, listAcertos
    PlotarGrafico()
    return
    # SimuladorMRU.MRU(textoMetodo[0],int(E1.get()))


def PlotarGrafico():
    ax.cla()
    ax.set(xlabel='Quantidade de Frames', ylabel='Quantidade de Acertos',title='Algoritmos de Substituição de Páginas')
    ax.grid(b='bool',which='major',axis='both',in_layout='bool')
    try:
        x1,y1=listFramesFifo,listAcertosFifo
        xx1=np.array(x1)
        yy1=np.array(y1)
        ax.plot(xx1, yy1, 'r-',label ='FIFO')
        
      
    except:
        None

    try:
        x2,y2=listFramesNUR,listAcertosNUR
        xx2=np.array(x2)
        yy2=np.array(y2)
        ax.plot(xx2, yy2, 'y-',label ='NUR')

    except:
        None

    try:
        x3,y3=listFramesMRU,listAcertosMRU
        xx3=np.array(x3)
        yy3=np.array(y3)
        ax.plot(xx3, yy3, 'g-',label ='MRU')
    except:
        None

    try:
        x4,y4=listFramesSegundaChance,listAcertosSegundaChance
        xx4=np.array(x4)
        yy4=np.array(y4)
        ax.plot(xx4, yy4, 'b-',label ='Segunda Chance' )
    except:
        None
 
    ax.legend()
    canva=FigureCanvasTkAgg(figura,App)
    canva.get_tk_widget().place(x=5,y=50)

def restart():
    App.destroy()
    os.startfile("Main.py")

def openFile():
    try:
        tf = filedialog.askopenfilename(
            initialdir="C:/Users/MainFrame/Desktop/",
            title="Open Text file",
            filetypes=(("Text Files", "*.txt"),)
        )

        tf = open(tf)
        data = tf.read()
        textoMetodo.extend(data)
        tf.close()
    except:
        None


def GetEntry():
    global Entrada1,Entrada2,ResetInterval,FramesAcertoGerais

    try:
        Entrada1,Entrada2=int(E1.get()), int(E2.get())
        ResetInterval= int(E4.get())
        FramesAcertoGerais=Entrada2-Entrada1+1
        if(Entrada1>1 and Entrada2>1 and textoMetodo!=[]):
            Controle.destroy()
            BotaoMetodos()
    except:
        None


def BotaoMetodos():
    ControleMetodo = Frame(App)
    ControleMetodo.place(x=5,y=550)

    ButtonFIFO = Button(ControleMetodo,text="Metodo Fifo",command=MetodoFIFO).pack(side="left", expand=False,padx=15,pady=5)

    ButtonSChance = Button(ControleMetodo,text="Metodo Segunda Chance",command=MetodoSegundaChance).pack(side="left", expand=False,padx=15,pady=5)

    ButtonNUR = Button(ControleMetodo,text="Metodo NUR",command=MetodoNUR).pack(side="left", expand=False,padx=15,pady=5)

    ButtonMRU = Button(ControleMetodo,text="Metodo MRU",command=MetodoMRU).pack(side="left", expand=False,padx=15,pady=5)

    LQ1 = Label(ControleMetodo, text=f"Frame Q1: {Entrada1} ")
    LQ1.pack( expand=FALSE,side=["left"], padx=5, pady=5)
    
    LQ2 = Label(ControleMetodo, text=f"Frame Q2: {Entrada2} ")
    LQ2.pack( expand=FALSE,side=["left"], padx=5, pady=5)

    LNUR = Label(ControleMetodo, text=f"Reset Interval: {ResetInterval}")
    LNUR.pack( expand=FALSE,side=["left"], padx=5, pady=5)

    ButtonRestart = Button(ControleMetodo,text="Restart",command=restart).pack(side="left", expand=False,padx=15,pady=5)

textoMetodo = []
textoAcertosNUR = []
textoAcertosFIFO = []
textoAcertosSegC = []
textoAcertosMRU = []

##################Tk########################
App = Tk()
App.title("PythonGuides")
App.geometry("1400x600")
App['bg'] = '#120a8f'
App.title('Simuladore De Memoria')
App.iconbitmap(r'F.ico')
#######################Tabela################################
game_frame = Frame(App)
game_frame.place(x=660,y=50)

#scrollbar

game_scroll = Scrollbar(game_frame,orient='horizontal')
game_scroll.pack(side= BOTTOM,fill=X)

game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)

my_game = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)


my_game.pack()

game_scroll.config(command=my_game.yview)
game_scroll.config(command=my_game.xview)

#define our column
 
my_game['columns'] = ('Frames_id', 'FIFO_id', 'Seg_Chance_id', 'NUR_id', 'MRU_id')

# format our column
my_game.column("#0", width=0,  stretch=NO)
my_game.column("Frames_id",anchor=CENTER, width=120)
my_game.column("FIFO_id",anchor=CENTER,width=120)
my_game.column("Seg_Chance_id",anchor=CENTER,width=120)
my_game.column("NUR_id",anchor=CENTER,width=120)
my_game.column("MRU_id",anchor=CENTER,width=120)

#Create Headings 
my_game.heading("#0",text="",anchor=CENTER)
my_game.heading("Frames_id",text="QUANTIDADE DE FRAMES",anchor=CENTER)
my_game.heading("FIFO_id",text="FIFO",anchor=CENTER)
my_game.heading("Seg_Chance_id",text="SEGUNDA CHANCE",anchor=CENTER)
my_game.heading("NUR_id",text="NUR",anchor=CENTER)
my_game.heading("MRU_id",text="MRU",anchor=CENTER)

#add data 
def tabela():
    #print(textoAcertosFIFO,textoAcertosNUR)
    listaFrameAcerto=Entrada1
    for i in range(FramesAcertoGerais):
        
        if(textoAcertosFIFO==[] or i>len(textoAcertosFIFO)-1):
            a=''
        else:
            a=textoAcertosFIFO[i]

        if(textoAcertosSegC==[] or i>len(textoAcertosSegC)-1):
            b=''
        else:
            b=textoAcertosSegC[i]

        if(textoAcertosNUR==[] or i>len(textoAcertosNUR)-1):
            c=''
        else:
            c=textoAcertosNUR[i]

        if(textoAcertosMRU==[] or i>len(textoAcertosMRU)-1):
            d=''
        else:
            d=textoAcertosMRU[i]
        
        try:
            my_game.delete(i)
            my_game.insert(parent='',index='end',iid=i,text='',values=(str(listaFrameAcerto+i),str(a),str(b),str(c),str(d)))
        except:
            my_game.insert(parent='',index='end',iid=i,text='',values=(str(listaFrameAcerto+i),str(a),str(b),str(c),str(d)))



#####################################################################

#Grafico inicial
figura = plt.Figure()
ax=figura.add_subplot(111)
canva=FigureCanvasTkAgg(figura,App)
canva.get_tk_widget().place(x=5,y=50)
ax.set(xlabel='Quantidade de Frames', ylabel='Quantidade de Acertos',title='Algoritmos de Substituição de Páginas')
ax.grid(b='bool',which='major',axis='both',in_layout='bool')

#######################

Controle = Frame(App)
Controle.place(x=5,y=550)

L1 = Label(Controle, text="Frame Q1 ")
L1.pack( expand=FALSE,side=["left"], padx=5, pady=5)

E1 = Entry(Controle,bd=5)
E1.pack(expand=FALSE, side=["left"], padx=5,pady=5)

L2 = Label(Controle, text="Frame Q2")
L2.pack(expand=FALSE, side=["left"], padx=5,pady=5)

E2 = Entry(Controle, bd=5)
E2.pack(expand=FALSE, side=["left"], padx=5,pady=5)


L4 = Label(Controle, text="Reset Interval")
L4.pack(expand=FALSE, side=["left"], padx=5,pady=5)

E4 = Entry(Controle, bd=5)
E4.pack(expand=FALSE, side=["left"], padx=5,pady=5)

ButtonOpenfile = Button(Controle,text="Open File",command=openFile)
ButtonOpenfile.pack(expand=FALSE, side=["left"], ipadx=22,padx=5,pady=5)

ButtonOK = Button(Controle,text="Ok",command=GetEntry)
ButtonOK.pack(expand=FALSE, side=["left"], ipadx=22,padx=5,pady=5)

App.mainloop()
