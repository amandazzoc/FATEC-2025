from flask import render_template, request, redirect, url_for
from models.database import db, Livro, Avaliacao
import urllib # envia requisições
import json # conversão de dados json

def init_app(app):
    wishList = ['Amor e Sorte', 'A divina comédia', 'A biblioteca da meia-noite']
    readBooks = [{
        'title': 'Harry Potter e a Pedra Filosofal',
        'pages': 223,
        'startDate': '2023-01-01',
        'endDate': '2023-01-15',
        'evaluation': 5
    }]

    def get_book_type_text(book_type):
        types = {
            1: "Lido",
            2: "Lendo",
            3: "Quero ler",
            4: "Relendo",
            5: "Abandonei"
        }
        return types.get(book_type, "Desconhecido")

    @app.route('/')
    def home():
        return render_template('home.html')
    
    # @app.route('/wishList', methods=['GET', 'POST'])
    # def wish_list_view():
    #     if request.method == 'POST':
    #         if request.form.get('book'):
    #             wishList.append(request.form.get('book'))
    #             return redirect(url_for('wish_list_view'))
    #     return render_template('wishList.html', wishList=wishList)
    
    # @app.route('/readBooks', methods=['GET', 'POST'])
    # def read_books():
    #     if request.method == 'POST':
    #         if (request.form.get('title') and request.form.get('pages') and 
    #             request.form.get('startDate') and request.form.get('endDate') and 
    #             request.form.get('evaluation')):
    #             readBooks.append({
    #                 'title': request.form.get('title'),
    #                 'pages': int(request.form.get('pages')),
    #                 'startDate': request.form.get('startDate'),
    #                 'endDate': request.form.get('endDate'),
    #                 'evaluation': int(request.form.get('evaluation'))
    #             })
    #             return redirect(url_for('read_books'))
    #     return render_template('readBooks.html', readBooks=readBooks)
    
    @app.route('/readBooks', methods=['GET', 'POST'])
    def read_books():
        from datetime import datetime
        if request.method == 'POST':
            # Adicionar avaliação
            titulo = request.form.get('title')
            paginas = request.form.get('pages')
            data_inicio = request.form.get('startDate')
            data_fim = request.form.get('endDate')
            nota = request.form.get('evaluation')
            if titulo and paginas and data_inicio and data_fim and nota:
                # Cria livro se não existir
                livro = Livro.query.filter_by(titulo=titulo).first()
                if not livro:
                    livro = Livro(titulo)
                    db.session.add(livro)
                    db.session.commit()
                avaliacao = Avaliacao(
                    livro_id=livro.id,
                    paginas_lidas=int(paginas),
                    data_inicio=datetime.strptime(data_inicio, '%Y-%m-%d'),
                    data_fim=datetime.strptime(data_fim, '%Y-%m-%d'),
                    nota=float(nota)
                )
                db.session.add(avaliacao)
                db.session.commit()
                return redirect(url_for('read_books'))
        # Listar avaliações
        avaliacoes = Avaliacao.query.all()
        readBooks = []
        for a in avaliacoes:
            readBooks.append({
                'id': a.id,
                'title': a.livro.titulo if a.livro else '',
                'pages': a.paginas_lidas,
                'startDate': a.data_inicio.strftime('%Y-%m-%d') if a.data_inicio else '',
                'endDate': a.data_fim.strftime('%Y-%m-%d') if a.data_fim else '',
                'evaluation': a.nota
            })
        livros = Livro.query.all()
        return render_template('readBooks.html', readBooks=readBooks, livros=livros)

    @app.route('/readBooks/edit/<int:id>', methods=['GET', 'POST'])
    def edit_avaliacao(id):
        from datetime import datetime
        avaliacao = Avaliacao.query.get(id)
        if not avaliacao:
            return redirect(url_for('read_books'))
        if request.method == 'POST':
            titulo = request.form.get('title')
            paginas = request.form.get('pages')
            data_inicio = request.form.get('startDate')
            data_fim = request.form.get('endDate')
            nota = request.form.get('evaluation')
            if titulo:
                livro = Livro.query.filter_by(titulo=titulo).first()
                if not livro:
                    livro = Livro(titulo)
                    db.session.add(livro)
                    db.session.commit()
                avaliacao.livro_id = livro.id
            if paginas:
                avaliacao.paginas_lidas = int(paginas)
            if data_inicio:
                avaliacao.data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')
            if data_fim:
                avaliacao.data_fim = datetime.strptime(data_fim, '%Y-%m-%d')
            if nota:
                avaliacao.nota = float(nota)
            db.session.commit()
            return redirect(url_for('read_books'))
        # GET: renderizar formulário de edição (pode ser ajustado no template depois)
        return render_template('editAvaliacao.html', avaliacao=avaliacao)

    @app.route('/readBooks/delete/<int:id>', methods=['POST'])
    def delete_avaliacao(id):
        avaliacao = Avaliacao.query.get(id)
        if avaliacao:
            db.session.delete(avaliacao)
            db.session.commit()
        return redirect(url_for('read_books'))
    
    @app.route('/wishList', methods=['GET', 'POST'])
    def wish_list_view():
        if request.method == 'POST':
            newLivro = Livro(request.form['book'])
            db.session.add(newLivro)
            db.session.commit()
            return redirect(url_for('wish_list_view'))
        else:
            page = request.args.get('page', 1, type=int)
            per_page = 4
            livros_page = Livro.query.paginate(page=page, per_page=per_page)
            livros = Livro.query.all()
            return render_template('wishList.html', livros=livros, livros_page=livros_page)

    @app.route('/wishList/edit/<int:id>', methods=['POST'])
    def wish_list_edit(id):
        livro = Livro.query.get(id)
        if livro and 'titulo' in request.form:
            livro.titulo = request.form['titulo']
            db.session.commit()
        return redirect(url_for('wish_list_view'))

    @app.route('/wishList/delete/<int:id>', methods=['POST'])
    def wish_list_delete(id):
        livro = Livro.query.get(id)
        db.session.delete(livro)
        db.session.commit()
        return redirect(url_for('wish_list_view'))
    
    @app.route('/estante', methods=['GET', 'POST'])
    @app.route('/estante/<int:id>', methods=['GET', 'POST'])
    def estante(id=None):
        url = 'https://skoob-api.onrender.com/api/users/8564121/bookshelf'
        response = urllib.request.urlopen(url)
        data = response.read()
        data = data.decode('utf-8')
        bookList = json.loads(data)
        
        if id:
            bookInfo = []
            for book in bookList:
                if book['edition']['id'] == id:
                    bookInfo = book
                    break
            if bookInfo:
                return render_template('book_detail.html', bookInfo=bookInfo)
            else:
                return "Livro não encontrado", 404
        else:
            for book in bookList:
                book['type_text'] = get_book_type_text(book['type'])

            return render_template('estante.html', bookList=bookList)