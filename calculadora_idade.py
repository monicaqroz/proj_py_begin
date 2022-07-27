from tkinter import *
from tkinter import ttk

#importar tkcalendar
from tkcalendar import Calendar, DateEntry

#importar dateutil
from dateutil.relativedelta import relativedelta

#importar datetime py 
from datetime import date

janela =Tk()
janela.title("Calculadora de Idade")
janela.geometry("310x400")

#cores
cor1 = "#fd7698" #rosa escuro
cor2 = "#ffffff" #branco
cor3 = "#000000" #preto
cor4 = "#8bd9ff"
cor5 = "#b89ae7"
cor6 = "#ffaad5"


#criando frames
frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=cor1)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=300, pady=0, padx=0, relief=FLAT, bg=cor6)
frame_baixo.grid(row=1, column=0)

#labels 
l_calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief=FLAT, anchor="center", font=('Evi 15 bold'), bg=cor1, fg=cor3)
l_calculadora.place(x=0,y=30)

l_idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief=FLAT, anchor="center", font=('Arial 35 bold'), bg=cor1, fg=cor4)
l_idade.place(x=0,y=70)

#calculos 
def calcular():
    inicial = cal_1.get()
    termino = cal_2.get()

    #separando valores e atributos 
    dia_1, mes_1, ano_1 = [int(f) for f in inicial.split("/")]
    data_inicial = date(ano_1, mes_1, dia_1)

    dia_2, mes_2, ano_2 = [int(f) for f in termino.split("/")]
    data_nascimento = date(ano_2, mes_2, dia_2)

    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days

    l_app_anos["text"] = anos
    l_app_meses["text"] = meses
    l_app_dias["text"] = dias

#labels frame baixo 

l_data_inicial = Label(frame_baixo, text="Data inicial", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Evi 11 bold'), bg=cor6, fg=cor3)
l_data_inicial.place(x=30,y=30)

cal_1 = DateEntry(frame_baixo, width=13, bg="darkblue", fg=cor3, borderwidth=2, date_patern="dd,mm,y", y=2022)
cal_1.place(x=180, y=30)

l_data_nascimento = Label(frame_baixo, text="Data de nascimento", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Evi 11 bold'), bg=cor6, fg=cor3)
l_data_nascimento.place(x=30,y=70)

cal_2 = DateEntry(frame_baixo, width=13, bg="darkblue", fg=cor3, borderwidth=2, date_patern="dd,mm,y", y=2022)
cal_2.place(x=180, y=70)

#labels resultados 

l_app_anos = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor="center", font=('Evi 25 bold'), bg=cor6, fg=cor3)
l_app_anos.place(x=60,y=135)
l_app_anos_nome = Label(frame_baixo, text="Anos", height=1, padx=0, pady=0, relief=FLAT, anchor="center", font=('Evi 11 bold'), bg=cor6, fg=cor1)
l_app_anos_nome.place(x=60,y=175)

l_app_meses = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor="center", font=('Evi 25 bold'), bg=cor6, fg=cor3)
l_app_meses.place(x=140,y=135)
l_app_meses_nome = Label(frame_baixo, text="Meses", height=1, padx=0, pady=0, relief=FLAT, anchor="center", font=('Evi 11 bold'), bg=cor6, fg=cor1)
l_app_meses_nome.place(x=135,y=175)

l_app_dias = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor="center", font=('Evi 25 bold'), bg=cor6, fg=cor3)
l_app_dias.place(x=220,y=135)
l_app_dias_nome = Label(frame_baixo, text="Dias", height=1, padx=0, pady=0, relief=FLAT, anchor="center", font=('Evi 11 bold'), bg=cor6, fg=cor1)
l_app_dias_nome.place(x=220,y=175)

#botão calcular 

b_calcular= Button(frame_baixo, text="Calcular", width=20, height=1, relief="raised", overrelief="ridge", font=('Evi 12 bold'), bg=cor1, fg=cor4, command=calcular)
b_calcular.place(x=50,y=210)


janela.mainloop()

