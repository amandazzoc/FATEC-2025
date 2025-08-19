from flask import Flask, render_template

# criando instância do flask
app = Flask(__name__, template_folder='views') # __name__ representa o nome da aplicação

# app.run() padrão
# app.run(host='localhost', port=5000, debug=True) mudar as configs padrões

# Definindo a rota principal da aplicação


@app.route('/')
def home(): # Função que será executada ao acessar a rota
    return render_template('index.html')


@app.route('/games')
def games():
    title = 'Tarisland'
    year = 2022
    category = 'MMORPG'
    players = ['Yan', 'Ferrari', 'Valéria', 'Amanda']
    console = {'name': 'Playstation',
               'manufacture': 'Sony',
               'year': 2020}
    return render_template('games.html', 
                           title = title,
                           year = year,
                           category = category,
                           players = players,
                           console = console)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

