from flask import Flask, render_template, request

# criando instância do flask
app = Flask(__name__, template_folder='views') # __name__ representa o nome da aplicação

# app.run() padrão
# app.run(host='localhost', port=5000, debug=True) mudar as configs padrões

# Definindo a rota principal da aplicação
def init_app(app):
    players = ['Yan', 'Ferrari', 'Valéria', 'Amanda']
    gamelist = [
        {'Título': 'Tarisland', 'Ano': 2022, 'Categoria': 'MMORPG'}
    ]

    @app.route('/')
    def home(): # Função que será executada ao acessar a rota
        return render_template('index.html')


    @app.route('/games', methods=['GET', 'POST'])
    def games():
        title = 'Tarisland'
        year = 2022
        category = 'MMORPG'
        # players = ['Yan', 'Ferrari', 'Valéria', 'Amanda'] mudando para o escopo global para ela adicionar e nao reiniciar
        console = {'name': 'Playstation',
                'manufacture': 'Sony',
                'year': 2020}
        
        # tratando uma requisicao POST com request
        if request.method == 'POST':
            # coletando o texto da input
            if request.form.get('player'):
                players.append(request.form.get('player'))
        
        return render_template('games.html', 
                            title = title,
                            year = year,
                            category = category,
                            players = players,
                            console = console)

    @app.route('/newGame', methods=['GET', 'POST'])
    def newGame():
        
        if request.method == 'POST':
            if request.form.get('title') and request.form.get('year') and request.form.get('category'):
                gamelist.append({'Título':request.form.get('title'), 'Ano': request.form.get('year'), 'Categoria': request.form.get('category')})
                
        return render_template('newGame.html', gamelist=gamelist)



