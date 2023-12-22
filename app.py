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
        return dados
    else:
        return {"error": "Nenhuma tabela encontrada na página"}

app = Flask(__name__)

@app.route('/api/v1/resultado', methods=['GET'])
def resultado():
    dados = buscaTabelaResultado('https://www.ojogodobicho.com/deu_no_poste.htm')
    return jsonify(dados)

# A remoção de app.run() é necessária quando usando Gunicorn

if __name__ == '__main__':
    app.run()
