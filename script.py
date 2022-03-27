import requests
from bs4 import BeautifulSoup

#MXL
def fundo_mxrf11():
    #cotacao
    #html_cotacao = requests.get("https://chart.fundsexplorer.com.br/chart/mxrf11/").content
    #soup = BeautifulSoup(html_cotacao, "html.parser")
    #cotacao = soup.find("span", class_="value")
    #print(cotacao.string)

    #ultimo dividendo
    html_dividendo = requests.get("https://www.fundsexplorer.com.br/funds/mxrf11").content
    soup1 = BeautifulSoup(html_dividendo, "html.parser")
    dividendo = soup1.find_all("div", class_="carousel-cell is-selected")
    #dividendo1 = dividendo.next_element
    print(dividendo.next_element)

    #tentando setar o caminho especifico do segundo elemento a ser analisado

fundo_mxrf11()