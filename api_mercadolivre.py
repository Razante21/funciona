# Supondo que você já tenha as importações necessárias
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error_message = ''
    search_results = []

    if request.method == 'POST':
        query = request.form.get('query')
        url = f'https://api.mercadolibre.com/sites/MLB/search?q={query}'
        
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            search_results = []

            for item in data['results']:
                product = {
                    'title': item['title'],
                    'price': f"{item['price']:.2f}".replace('.', ','),
                    'link': item['permalink'],
                    'image': item['thumbnail']
                }
                search_results.append(product)
        else:
            error_message = 'Ocorreu um erro ao buscar os produtos.'

    return render_template('index.html', search_results=search_results, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
