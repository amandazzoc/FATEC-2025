from flask import Flask, render_template, request, redirect, url_for
import urllib # envia requisições
import json # conversão de dados json
from models.database import Game, db

def init_app(app):
    # lista 
    # a lista veio pra cá pq dentro da função ela era reiniciada a cada requisição
    players = ['Giovana', 'Amanda', 'Igor', 'Diego']
    gamelist = [{'Título': 'CS 1.6', 'Ano': 1996, 'Categoria': 'FPS Online'}]
    
    
    # definindo a rota principal da aplicação '/'
    @app.route('/')
    # toda rota precisa de um função para executar 
    def home():
        return render_template('index.html')


    # definindo a rota principal da aplicação '/'
    @app.route('/games', methods=['GET', 'POST'])
    # toda rota precisa de um função para executar 
    def games():
        # essas variáveis estariam vindo de fora 
        title = 'Tarisland'
        year = 2022
        category = 'MMORPG'
        # dicionário 
        console = {'Nome' : 'PS5', 'Fabricante': 'Sony', 'Ano': 2020}
        
        # tratando uma requisição POST com request
        if request.method == 'POST':
            # coletando o texto da input 
            # player é o nome da caixinha que eu criei no form
            if request.form.get('player'):
                players.append(request.form.get('player'))
                return redirect(url_for('games'))
        
        # o primeiro title é a var que vai ser criada na página 
        return render_template('games.html', title=title, year=year, category=category, players=players, console=console)
    
    
    @app.route('/newGame', methods=['GET', 'POST'])
    def newGame():
        if request.method == 'POST':
            if request.form.get('title') and request.form.get('year') and request.form.get('category'):
                gamelist.append({'Título': request.form.get('title'), 'Ano': request.form.get('year'), 'Categoria' : request.form.get('category')})
                return redirect(url_for('newGame'))
                
        return render_template('newGame.html', gamelist=gamelist)
    
    
    @app.route('/apigames', methods=['GET', 'POST'])
    # Criando parâmetros para a rota
    # Para string <id>
    # Para int <int:id>
    @app.route('/apigames/<int:id>', methods=['GET', 'POST'])
    def apigames(id=None): # parâmetro opcional
        url = 'https://www.freetogame.com/api/games' # seta a url  
        response = urllib.request.urlopen(url) # faz request abrindo a url
        data = response.read() # le os dados
        gameList = json.loads(data) # transforma os dados em um dicionario
        # verificando se o parâmetro foi enviado
        if id:
            gameInfo = []
            for game in gameList:
                if game['id'] == id: # Comparando os IDs
                    gameInfo = game
                    break
            if gameInfo:
                return render_template('gameinfo.html', gameInfo=gameInfo)
            else: return f'Game com a id {id} não foi encontrado.'
        else: 
            return render_template('apigames.html', gameList=gameList)
        
    @app.route('/estoque', methods=['GET', 'POST'])
    @app.route('/estoque/delete/<int:id>', methods=['POST'])
    def estoque(id=None):
        # Verifica se o ID foi passado para deletar o jogo
        if id:
            game = Game.query.get(id)
            
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque'))
        
        if request.method == 'POST':
            # Realiza o cadastro do jogo
            newGame = Game(request.form['title'], request.form['year'], request.form['category'], request.form['platform'], float(request.form['price']), int(request.form['quantity']))
            
            # Adiciona o novo jogo na sessão do banco
            db.session.add(newGame)
            # Confirma a adição no banco
            db.session.commit()
        
        # Busca todos os jogos no banco de dados
        gameEstoque = Game.query.all()
        return render_template('estoque.html', gameEstoque=gameEstoque)