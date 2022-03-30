from cgitb import text
import re
from sqlite3 import Row
from tkinter import *
from tkinter.tix import COLUMN
from turtle import width
from bs4 import BeautifulSoup
import requests
import soupsieve
from tkinter.tix import COLUMN

#========FUNÇÕES===========
#Função referente ao MXRF11
def fundo_mxrf11():
    html_cotacao = requests.get("https://chart.fundsexplorer.com.br/chart/mxrf11/").content
    soup = BeautifulSoup(html_cotacao, "html.parser")
    cotacao = soup.find("span", class_="value")
    cotacao_mxrf11 = cotacao.string
    cota_mxrf["text"] = cotacao_mxrf11

#Função referente ao KNRI11
def fundo_knri11():
    html_cotacao = requests.get("https://chart.fundsexplorer.com.br/chart/knri11/").content
    soup = BeautifulSoup(html_cotacao, "html.parser")
    cotacao = soup.find("span", class_="value")
    cotacao_knri11 = cotacao.string
    cota_knri["text"] = cotacao_knri11

#Função referente ao HGLG11
def fundo_hglg11():
    html_cotacao = requests.get("https://chart.fundsexplorer.com.br/chart/hglg11/").content
    soup = BeautifulSoup(html_cotacao, "html.parser")
    cotacao = soup.find("span", class_="value")
    cotacao_hglg11 = cotacao.string
    cota_hglg["text"] = cotacao_hglg11

#Função referente ao BCFF11
def fundo_bcff11():
    html_cotacao = requests.get("https://chart.fundsexplorer.com.br/chart/bcff11/").content
    soup = BeautifulSoup(html_cotacao, "html.parser")
    cotacao = soup.find("span", class_="value")
    cotacao_bcff11 = cotacao.string
    cota_bcff["text"] = cotacao_bcff11

#============GUI============
janela = Tk()
janela.geometry("400x350")
janela.title("Cotação dos Fundos Imobiliarios")

descricao = Label(janela, text="COTAÇÕES").grid(column=1, row=0, padx=50)
descricaoF = Label(janela, text="FUNDOS").grid(column=0, row=0, padx=20)

#GUI KNRI11
knri = Label(janela, text="Fundo KNRI11:").grid(column=0, row=1, padx=30)
cota_knri = Label(janela, text="")
cota_knri.grid(column=1, row=1)
botao_knri = Button(janela, text="Atualizar", command=fundo_knri11)
botao_knri.grid(column=2, row=1)

#GUI MXRF11
mxrf = Label(janela, text="Fundo MXRF11:").grid(column=0, row=2, pady=5)
cota_mxrf = Label(janela, text="")
cota_mxrf.grid(column=1, row=2, pady=5)
botao_mxrf = Button(janela, text="Atualizar", command=fundo_mxrf11)
botao_mxrf.grid(column=2, row=2, pady=5)

#GUI HGLG11
hglg = Label(janela, text="Fundo HGLG11:").grid(column=0, row=3)
cota_hglg = Label (janela, text="")
cota_hglg.grid(column=1, row=3)
botao_hglg = Button(janela, text="Atualizar", command=fundo_hglg11)
botao_hglg.grid(column=2, row=3)

#GUI BCFF11
hglg = Label(janela, text="Fundo BCFF11:").grid(column=0, row=4, pady=5)
cota_bcff = Label (janela, text="")
cota_bcff.grid(column=1, row=3, pady=5)
botao_bcff = Button(janela, text="Atualizar", command=fundo_bcff11)
botao_bcff.grid(column=2, row=4, pady=5) 

sair = Button(janela, text="Sair", command=janela.quit)
sair.grid(column=1, row=10, ipadx= 35, pady= 25)
janela.mainloop()