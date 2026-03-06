#importando tkinter
from tkinter import *
from tkinter import ttk

#cores 
cor1 = "#1c1c1c" # preto
cor2 = "#3d3d3d" # cinza
cor3 = "#838385" # cinza mais claro
cor4 = "#fac002" # amarelo alaranjado
cor5 = "#ffffff" # Branco

#criando janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg= cor1)

#dividinho a janela/ criando frames
frame_display = Frame(janela, width=235, height=50,bg = cor1 )
frame_display.grid(row = 0, column=0)

frame_botoes = Frame(janela, width=235, height=268,bg = cor1)
frame_botoes.grid(row = 1, column=0)

#variavel todos valores
todos_valores = ''
valor_texto = StringVar()

#Criando função

def entrada(evento):
    global todos_valores 
    todos_valores = todos_valores + str(evento)
    #passando o valor para o display
    valor_texto.set(todos_valores)

#Para calcular
def calcular ():
    global todos_valores
    try:
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))
        todos_valores = str(resultado)
    except Exception as e:
        valor_texto.set('Erro')
        todos_valores = ""
    
#Para limpar o Display
def limpar_display():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")
    
#Criando backspace
def backspace():
    global todos_valores
    todos_valores = todos_valores[:-1]
    valor_texto.set(todos_valores)

#Criando os números no display
app_label = Label(frame_display,textvariable=valor_texto, width=16, height=2, padx=7,relief=FLAT, anchor = "e" ,justify= RIGHT,font = "Ivy 18",bg=cor1,fg=cor5 )
app_label.place(x=0,y=0)


#criando botões
bt_0 = Button(frame_botoes,command=limpar_display, text="AC", width=5, height= 2, bg=cor3, font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE)
bt_0.place(x=0,y=0)
bt_1 = Button(frame_botoes,command= backspace, text = "⌫",width=5, height= 2, bg = cor3, font = ("Ivy 13 bold"),relief = RAISED, overrelief=RIDGE )
bt_1.place(x=59,y=0)
bt_2 = Button(frame_botoes, command= lambda:entrada('%'), text="%", width=5, height= 2, bg = cor3,font =("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_2.place(x=118,y=0)
bt_3 = Button(frame_botoes, command= lambda:entrada('/'), text="/", width=5, height= 2,bg = cor4,fg = cor5,font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_3.place(x=177,y=0)

bt_4 = Button(frame_botoes,command= lambda:entrada('7'), text="7", width=5, height= 2, bg = cor2,fg = cor5, font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_4.place(x=0,y=52)
bt_5 = Button(frame_botoes,command= lambda:entrada('8'), text="8", width=5, height= 2, bg = cor2,fg = cor5, font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_5.place(x=59,y=52)
bt_6 = Button(frame_botoes,command= lambda:entrada('9'), text="9", width=5, height= 2, bg = cor2,fg = cor5, font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_6.place(x=118,y=52)
bt_7 = Button(frame_botoes,command= lambda:entrada('*'), text="*", width=5, height= 2,bg = cor4,fg = cor5,font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_7.place(x=177,y=52)

bt_8 = Button(frame_botoes,command= lambda:entrada('4'), text="4", width=5, height= 2, bg = cor2,fg = cor5, font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_8.place(x=0,y=104)
bt_9 = Button(frame_botoes, command= lambda:entrada('5'),text="5", width=5, height= 2, bg = cor2,fg = cor5, font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_9.place(x=59,y=104)
bt_10 = Button(frame_botoes, command= lambda:entrada('6'),text="6", width=5, height= 2, bg = cor2,fg = cor5, font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_10.place(x=118,y=104)
bt_11 = Button(frame_botoes,command= lambda:entrada('-'), text="-", width=5, height= 2,bg = cor4,fg = cor5,font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_11.place(x=177,y=104)

bt_12 = Button(frame_botoes,command= lambda:entrada('1'), text="1", width=5, height= 2, bg = cor2,fg = cor5, font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_12.place(x=0,y=156)
bt_13 = Button(frame_botoes,command= lambda:entrada('2'), text="2", width=5, height= 2, bg = cor2,fg = cor5, font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_13.place(x=59,y=156)
bt_14 = Button(frame_botoes, command= lambda:entrada('3'),text="3", width=5, height= 2, bg = cor2,fg = cor5, font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_14.place(x=118,y=156)
bt_15 = Button(frame_botoes,command= lambda:entrada('+'), text="+", width=5, height= 2,bg = cor4,fg = cor5,font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_15.place(x=177,y=156)

bt_16 = Button(frame_botoes,command= lambda:entrada('0'), text="0", width=11, height= 2, bg=cor2,fg = cor5, font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE)
bt_16.place(x=0,y=208)
bt_17 = Button(frame_botoes,command= lambda:entrada('.'), text=".", width=5, height= 2, bg = cor2,fg = cor5,font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_17.place(x=118,y=208)
bt_18 = Button(frame_botoes,command= calcular, text="=", width=5, height= 2,bg = cor4,fg = cor5,font = ("Ivy 13 bold"), relief = RAISED, overrelief=RIDGE )
bt_18.place(x=177,y=208)


janela.mainloop()