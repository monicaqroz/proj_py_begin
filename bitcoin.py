from tkinter import *
from tkinter import ttk 
from PIL import ImageTk, Image 

#importando bibliotecas api
import requests
import time
import json

#cores
cor1 = "#000000"
cor2 = "#ffffff"
cor3 = "#ff911a"
cor4 = "#969395"

#criando janela 
janela = Tk()
janela.title("Bitcoin Price Tracker")
janela.geometry("320x350")
janela.configure(bg=cor4)

#separador janela
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

#frames
frame_cima = Frame(janela, width=320, height=50, bg=cor2, pady=0, padx=0, relief=FLAT)
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=320, height=300, bg=cor1, pady=0, padx=0, relief=FLAT)
frame_baixo.grid(row=2, column=0, sticky=NW)

#função dados 
def info ():

#api link
    api_link = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,BRL"

    response = requests.get(api_link)

    dados = response.json()

    #dolar
    valor_usd = float(dados["USD"])
    valor_formatado_usd =" $ {:,.3f}".format(valor_usd)
    l_p_usd["text"] = "USD" + valor_formatado_usd

    valor_euro = float(dados["EUR"])
    valor_formatado_euro =" Є {:,.3f}".format(valor_euro)
    l_p_euro["text"] = "Em euro: EUR " + valor_formatado_euro

    valor_real = float(dados["BRL"])
    valor_formatado_real =" R$ {:,.3f}".format(valor_real)
    l_p_real["text"] = "Em real: BRL " + valor_formatado_real

    frame_baixo.after(1000, info)


#configurando frame cima
imagem = Image.open("imagens/bit1.png")
imagem = imagem.resize((30,30))
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_cima, image= imagem, compound=LEFT, bg=cor2, relief=FLAT)
l_icon.place(x=10, y=10)

l_nome = Label(frame_cima, text="Bitcoin Price Tracker", bg=cor2, fg=cor1, relief=FLAT, anchor="center", font=("Arial 20"))
l_nome.place(x=50, y=5)

#configurando frame baixo

l_p_usd = Label(frame_baixo, text="", bg=cor1, fg=cor3, relief=FLAT, anchor="center", font=("Arial 20"))
l_p_usd.place(x=10, y=50)

l_p_euro = Label(frame_baixo, text="", bg=cor1, fg=cor2, relief=FLAT, anchor="center", font=("Arial 12"))
l_p_euro.place(x=10, y=130)

l_p_real = Label(frame_baixo, text="",  bg=cor1, fg=cor2, relief=FLAT, anchor="center", font=("Arial 12"))
l_p_real.place(x=10, y=160)

info()

janela.mainloop()