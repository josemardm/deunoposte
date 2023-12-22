from flask import Flask, jsonify
import pandas as pd
import requests
from bs4 import BeautifulSoup


def buscaTabelaResultado(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    tabela = soup.find('table')

    if tabela:
        df = pd.read_html(str(tabela))[0]
        dados = df.to_dict(orient='records')

        dadosPTM = {}
        dadosPT = {}
        dadosPTV = {}
        dadosPTN = {}
        dadosCOR = {}

        for index in range(len(dados)):  # Alteração aqui

            dadosPTM[index] = dados[index]['PTM']
            dadosPT[index] = dados[index]['PT']
            dadosPTV[index] = dados[index]['PTV']
            dadosPTN[index] = dados[index]['PTN']
            dadosCOR[index] = dados[index]['COR']

        resultado = [dadosPTM, dadosPT, dadosPTV, dadosPTN, dadosCOR]

        return resultado
    else:
        return {"error": "Nenhuma tabela encontrada na página"}


app = Flask(__name__)


@app.route('/api/v1/resultado', methods=['GET'])
def resultado():
    dados = buscaTabelaResultado('https://www.ojogodobicho.com/deu_no_poste.htm')
    return jsonify(dados)


if __name__ == '__main__':
    app.run()
