from flask import render_template, request, redirect, url_for

def init_app(app):
    wishList = ['Amor e Sorte', 'A divina comédia', 'A biblioteca da meia-noite']
    readBooks = [{
        'title': 'Harry Potter e a Pedra Filosofal',
        'pages': 223,
        'startDate': '2023-01-01',
        'endDate': '2023-01-15',
        'evaluation': 5
    }]
    
    @app.route('/')
    def home():
        return render_template('home.html')
    
    @app.route('/wishList', methods=['GET', 'POST'])
    def wish_list_view():
        if request.method == 'POST':
            if request.form.get('book'):
                wishList.append(request.form.get('book'))
                return redirect(url_for('wish_list_view'))
        return render_template('wishList.html', wishList=wishList)
    
    @app.route('/readBooks', methods=['GET', 'POST'])
    def read_books():
        if request.method == 'POST':
            if (request.form.get('title') and request.form.get('pages') and 
                request.form.get('startDate') and request.form.get('endDate') and 
                request.form.get('evaluation')):
                readBooks.append({
                    'title': request.form.get('title'),
                    'pages': int(request.form.get('pages')),
                    'startDate': request.form.get('startDate'),
                    'endDate': request.form.get('endDate'),
                    'evaluation': int(request.form.get('evaluation'))
                })
                return redirect(url_for('read_books'))
        return render_template('readBooks.html', readBooks=readBooks)