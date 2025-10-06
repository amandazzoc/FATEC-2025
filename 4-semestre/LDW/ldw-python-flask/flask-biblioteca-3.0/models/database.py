from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    
    def __init__(self, titulo):
        self.titulo = titulo
        
class Avaliacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    livro_id = db.Column(db.Integer, db.ForeignKey('livro.id'))
    paginas_lidas = db.Column(db.Integer)
    data_inicio = db.Column(db.Date)
    data_fim = db.Column(db.Date)
    nota = db.Column(db.Float)

    livro = db.relationship('Livro', backref=db.backref('avaliacoes', lazy=True))
    
    """ livro_id = db.Column(db.Integer, db.ForeignKey('livro.id'))
    livro = db.relationship('Livro', backref=db.backref('avaliacoes', lazy=True))
    """
    
    def __init__(self, livro_id, paginas_lidas, data_inicio, data_fim, nota):
        self.livro_id = livro_id
        self.paginas_lidas = paginas_lidas
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.nota = nota