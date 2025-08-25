from flask import Flask, render_template
from controllers import routes

# criando instância do flask
app = Flask(__name__, template_folder='views') # __name__ representa o nome da aplicação

# app.run() padrão
# app.run(host='localhost', port=5000, debug=True) mudar as configs padrões
routes.init_app(app)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

