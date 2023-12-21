from flask import Flask, jsonify
import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO  # Importe StringIO da biblioteca io


def buscaTabelaResultado(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')
    # Encontre a tabela
    tabela = soup.findAll('table')
    df = pd.read_html(StringIO(str(tabela)))[0]
    array_resultado = df.to_numpy()  # Converte o DataFrame para um array NumPy
    return array_resultado.tolist()  # Converte o array NumPy para uma lista Python


app = Flask(__name__)


@app.route('/api/v1/resultado', methods=['GET'])
def resultado():
    dados = buscaTabelaResultado('https://www.ojogodobicho.com/deu_no_poste.htm')
    return jsonify(dados)


if __name__ == '__main__':
    app.run(port=80)
