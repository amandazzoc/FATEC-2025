# Importando o Flask
from flask import Flask, render_template
# Importando o Controller (routes.py)
from controllers import routes
# Importando os Models
from models.database import db
# Importando a biblioteca para manipulação de S.O
import os

# Criando uma instância do Flask 
app = Flask(__name__, template_folder='views') # esse parâmetro representa o nome da aplicação

routes.init_app(app)

# Extraindo o diretório absoluto do arquivo
dir = os.path.abspath(os.path.dirname(__file__))

# Criando o arquivo do banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir, 'models/games.sqlite3')

# se for executado diretamente pelo interpretador 
# camada de segurança; se eu importar o app em outro arquivo, não vai rodar o servidor;
if __name__ == '__main__':
    # Enviando o Flask para o SQLAlchemy
    db.init_app(app=app)
    
    # Verificar no início da aplicação se o BD já existe. Se não, ele cria.
    with app.test_request_context():
        db.create_all() 
        
    # iniciando o servidor
    app.run(host="localhost", port=5000, debug=True) 