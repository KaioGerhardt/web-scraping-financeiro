from pydoc import describe
from tkinter import *
import script
from bs4 import BeautifulSoup
import requests
#====================================
def fundo_knri11():
    #cotacao
    html_cotacao = requests.get("https://chart.fundsexplorer.com.br/chart/knri11/").content
    soup = BeautifulSoup(html_cotacao, "html.parser")
    cotacao = soup.find("span", class_="value")
    cotacao_final = cotacao.string
    #print(cotacao_final)
    #fundo_knri11()
    cotacao_knri11["text"] = cotacao_final

#=====================================

janela = Tk()
janela.title("Cotação de Fundos Imobiliarios")
janela.geometry("500x200")

descricao = Label(janela, text="Cotações atualizadas dos principais Fundos Imobiliários")
descricao.grid(column=1, row=0)

nome_knri11 = Label(janela, text="Fundo KNRI11:")
nome_knri11.grid(column=0, row=1)

cotacao_knri11 = Label(janela, text="")
cotacao_knri11.grid(column=1, row=1)

botao_teste = Button(janela, text="teste", command="fundo_knri11")
botao_teste.grid(column=3, row=4)

janela.mainloop()