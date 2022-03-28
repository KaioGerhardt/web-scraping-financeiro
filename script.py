import requests
from bs4 import BeautifulSoup
from gui import *

#MXL
def fundo_mxrf11():
    #cotacao
    html_cotacao = requests.get("https://chart.fundsexplorer.com.br/chart/mxrf11/").content
    soup = BeautifulSoup(html_cotacao, "html.parser")
    cotacao = soup.find("span", class_="value")
    cotacao_final = cotacao.string
    print(cotacao_final)

def fundo_knri11():
    #cotacao
    html_cotacao = requests.get("https://chart.fundsexplorer.com.br/chart/knri11/").content
    soup = BeautifulSoup(html_cotacao, "html.parser")
    cotacao = soup.find("span", class_="value")
    cotacao_final = cotacao.string
    print(cotacao_final)
    #fundo_knri11()
    cotacao_knri11["text"] = cotacao_final


if (__name__ == "__main__"):
    #testes
    fundo_mxrf11()
    fundo_knri11()