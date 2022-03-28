from cgitb import text
from tkinter import *
from bs4 import BeautifulSoup
import requests

#========FUNÇÕES===========
#Função referente ao MXRF11
def fundo_mxrf11():
    html_cotacao = requests.get("https://chart.fundsexplorer.com.br/chart/mxrf11/").content
    soup = BeautifulSoup(html_cotacao, "html.parser")
    cotacao = soup.find("span", class_="value")
    cotacao_mxrf11 = cotacao.string

#Função referente ao KNRI11
def fundo_knri11(botao_teste):
    html_cotacao = requests.get("https://chart.fundsexplorer.com.br/chart/knri11/").content
    soup = BeautifulSoup(html_cotacao, "html.parser")
    cotacao = soup.find("span", class_="value")
    cotacao_knri11 = cotacao.string


#============GUI============
janela = Tk()
janela.geometry("400x350")
janela.title("Cotação dos Fundos Imobiliarios")

descricao = Label(janela, text="Cotação dos Fundos Imobiliarios").grid(column=0, row=0)

janela.mainloop()