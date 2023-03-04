#imports
from tkinter import *
from tkinter import ttk

#janela
window = Tk()
window.title ('Calculator')
window.geometry ("450x465")


#CORES
cinza = '#22232e'
branco = '#fcfbf7'
laranja = '#d99a09'
azul = '#323754'


#Divisoes
divisao1 = Frame(window, width=450 , height=100)
divisao1.grid(row = 0 , column= 0)
divisao1.config(bg=cinza)

divisao2 = Frame(window, width=450 , height=365)
divisao2.grid(row = 1 , column= 0)
divisao2.config(bg=cinza)



#Monitor
resultado = StringVar()
show=""

monitor = Label(divisao1, textvariable= resultado, width=20 , height=1, anchor="e", bg=cinza, fg= branco, justify=RIGHT, font=('Ivy 25 bold'))
monitor.place(x= 40, y= 50)



#Função que adiciona o valor do botao pressionado ao monitor
def butPress(num):
    global show
    if show == '0':
        if num == ".":
            pass
        else:
            show = ""
    show = show + str(num)
    resultado.set(show)


# Função para calcular
def evaluate():
    global show
    resultado.set(show)
    total = str(eval(show))
    if len(total) > 20:
        total = str(total[0:20])
    resultado.set(total)
    show= total


#Função para dar clear
def clear():
    global show
    show = "0"
    resultado.set(show)


#Função para o del
def back():
    global show

    t = len(show)
    x = len(show)-2


    if (len(show)==1):
        res = ""
    elif (len(show)==2):
        res = show[len(show)-2]

    for i in range (0,x+1):
        if (i==0):
            res = show[0]
        else:
            res = res + show[len(show)-t+i]

    show = res

    resultado.set(show)



#####Botoes de numeros

zeru = Button(divisao2, text="0", width=10, height=3, command= lambda:butPress("0") , bg=azul, fg=branco,font=('Ivy 13 bold'))
zeru.place(x=113 , y = 292)

um = Button(divisao2, text="1", width=10, height=3, command= lambda:butPress("1") , bg=azul, fg=branco,font=('Ivy 13 bold'))
um.place(x=0 , y = 219)

dois = Button(divisao2, text="2", width=10, height=3, command= lambda:butPress("2") , bg=azul, fg=branco,font=('Ivy 13 bold'))
dois.place(x=113 , y = 219)

tres = Button(divisao2, text="3", width=10, height=3, command= lambda:butPress("3") , bg=azul, fg=branco,font=('Ivy 13 bold'))
tres.place(x=226 , y = 219)

quatro = Button(divisao2, text="4", width=10, height=3, command= lambda:butPress("4") , bg=azul, fg=branco,font=('Ivy 13 bold'))
quatro.place(x=0 , y = 146)

cinco = Button(divisao2, text="5", width=10, height=3, command= lambda:butPress("5") , bg=azul, fg=branco,font=('Ivy 13 bold'))
cinco.place(x=113 , y = 146)

seis = Button(divisao2, text="6", width=10, height=3, command= lambda:butPress("6") , bg=azul, fg=branco,font=('Ivy 13 bold'))
seis.place(x=226 , y = 146)

sete = Button(divisao2, text="7", width=10, height=3, command= lambda:butPress("7") , bg=azul, fg=branco,font=('Ivy 13 bold'))
sete.place(x=0 , y = 73)

oito = Button(divisao2, text="8", width=10, height=3, command= lambda:butPress("8") , bg=azul, fg=branco,font=('Ivy 13 bold'))
oito.place(x=113 , y = 73)

nove = Button(divisao2, text="9", width=10, height=3, command= lambda:butPress("9") , bg=azul, fg=branco,font=('Ivy 13 bold'))
nove.place(x=226 , y = 73)



#####Butoes de sinais

igual = Button(divisao2, text="=", width=10, height=7, command= evaluate , bg=laranja, fg=branco,font=('Ivy 13 bold'))
igual.place(x=340 , y = 219)

c = Button(divisao2, text="C", width=10, height=3, command= clear , bg=azul, fg=laranja,font=('Ivy 13 bold'))
c.place(x=0 , y = 0)

div = Button(divisao2, text="÷", width=10, height=3, command= lambda:butPress("/"), bg=azul, fg=laranja,font=('Ivy 13 bold'))
div.place(x=113 , y = 0)

mult= Button(divisao2, text="X", width=10, height=3, command= lambda:butPress("*"), bg=azul, fg=laranja,font=('Ivy 13 bold'))
mult.place(x=226 , y = 0)

dele = Button(divisao2, text="⌫", width=10, height=3, command= back , bg=laranja, fg=branco,font=('Ivy 13 bold'))
dele.place(x=340 , y = 0)

sub= Button(divisao2, text="-", width=10, height=3, command= lambda:butPress("-") , bg=laranja, fg=branco,font=('Ivy 13 bold'))
sub.place(x=340 , y = 73)

soma = Button(divisao2, text="+", width=10, height=3, command= lambda:butPress("+") , bg=laranja, fg=branco,font=('Ivy 13 bold'))
soma.place(x=340 , y = 146)

ponto = Button(divisao2, text=".", width=10, height=3, command= lambda:butPress(".") , bg=azul, fg=branco,font=('Ivy 13 bold'))
ponto.place(x=0 , y = 292)

per = Button(divisao2, text="%", width=10, height=3, command= lambda:butPress("/100") , bg=azul, fg=branco,font=('Ivy 13 bold'))
per.place(x=226 , y = 292)


window.mainloop()