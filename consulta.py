'''
utilizamos a função get do requests para acessar o servidor da API onde se encontram as informações das moedas:
A variável status_ code do requests é preenchida com a resposta http do servidor e a variável content também do
request, é preenchida com o conteúdo da API (JSON) 
utilizamos a biblioteca jason para converter os dados recebidos em um dicionario
'''

import requests
import json
import pandas
def converter_data(dia):
    dia = dia[8:]+"/"+dia[5:7]+"/"+dia [0:4]
    print("ultima atualização dos dados:", dia)
    return dia
def chave_acesso(chave="0d5bcbcf370dc3ca6c345472c79c1ad5&format"):
    return "http://data.fixer.io/api/latest?access_key=" + chave
def converter_em_reais(valor_real, valor_estrangeiro):
    return round(valor_real/valor_estrangeiro,2)
def exportar_tabela(lista_titulo, lista_valores, nome_arquivo, lista_dia):
    celulas = pandas.DataFrame({'Moedas':lista_titulo, 
    "Valores": lista_valores, "acessaso ": lista_dia})
    celulas.to_csv(nome_arquivo + ".csv", index=False, sep=";")
    print("tabela exportada com sucesso")


def main():
    chave = input("informe a chave de acesso do Fixer.io, se nao tiver aperte enter")
    url = "http://data.fixer.io/api/latest?access_key=0d5bcbcf370dc3ca6c345472c79c1ad5&format=1"
    print("acessando base de dados...")
    resposta=requests.get(url)
    if resposta.status_code==200:
        print("conexão com a base de dados estabelecida com sucesso")
        dados = resposta.json()
        #A função converter_data irá receber o valor da variável dados['date] e irá retornar a data convertida 
        #no padrão Brasil , que será atribuída a variável dia_convertido.
        dados = resposta.json()
        dia_convertido = converter_data(dados['date'])
        euro_em_reais = round(dados['rates'] ['BRL']/dados['rates'] ['EUR'],2)
        bitcoin_em_reais = round(dados['rates']['BRL']/dados['rates']['BTC'],2)
        dolar_em_reais = round(dados['rates'] ['BRL']/dados['rates'] ['USD'],2)
        escolha = input("digite:\nB - Bitcoin\nD - Dolar\nE - Euro\nA - Todas").upper()
        if (escolha=='B'):
            exportar_tabela (['Bitcoin'], [bitcoin_em_reais], 'bitcoin', [dia_convertido])
        elif (escolha=='D'):
            exportar_tabela (['Dolar'], [dolar_em_reais], 'dolar', [dia_convertido])
        elif (escolha=='E'):
            exportar_tabela (['Euro'], [bitcoin_em_reais], 'euro', [dia_convertido])
        elif (escolha=='A'):
            exportar_tabela (['Bitcoin', 'Dolar', 'Euro'], [bitcoin_em_reais, dolar_em_reais, euro_em_reais], 'moedas', [dia_convertido, "",""])
        else:
            print("voce não escolheu nenhum das opções. sua tabela não sera exportada")
    
        #No panda a chave do dicionario é o titulo da coluna e a litsa é o conteudo da coluna
        #Precisa do import pandas
        
        print("1 euro vale", euro_em_reais, "reais")
        print("1 bit coin", bitcoin_em_reais, "reais")
        print("1 dolar", dolar_em_reais, "reais")
    else:
        print ("erro ao acessar a base de dados")
    

if __name__=='__main__':
    main()
