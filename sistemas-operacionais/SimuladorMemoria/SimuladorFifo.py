
def FIFO(Dado="7W-2W-7R-4W-4R-2R-6R-6R-5W-2W-7R-0R-5W-6W-4R-5R-1R-1W-5W-",memoriaFisica = 4,memoriaFisicaMax=5):
    listFrames=[]
    listAcertos=[]
    loop=memoriaFisicaMax-memoriaFisica
    Referencia=Dado


    Referencia = Referencia.replace('R',"")
    Referencia = Referencia.replace('W',"")
    Referencia = Referencia.split('-')

    for i in range(loop):
        memoriaFisica=memoriaFisica+1
        fisica=[]
        m = 0
        c = 0
        acertos = 0
        erros = 0
        contador = 0
        flag = True

        if(Referencia[-1]==''):
            del Referencia[-1]
        
        while(True):
            if(c==memoriaFisica):
                break
            fisica.append("-")
            c=c+1


        while(True):
            if(m>=len(Referencia)):
                break
            contador=contador+1
            flag=True
            #print("\n"+Referencia[m])
            i=0
            for i in range(len(fisica)):
                a=Referencia[m]
                a
                b=fisica[i]
                if(a==b):
                    acertos=acertos + 1
                    flag=False

            if(flag==True):
                erros=erros+1
                del fisica[0]
                fisica.extend(" ")
                fisica[len(fisica)-1]=Referencia[m]
                #print(fisica)
            m=m+1

        listFrames.append(memoriaFisica)
        listAcertos.append(acertos)

    #print(fisica,"\nAcertos: ",acertos,"\nErros: ",erros,"\nContador :", contador )

    #print(listFrames,listAcertos)
    return listAcertos
