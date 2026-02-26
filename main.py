from flask  import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

with app.app_context():
    db.create_all()

@app.route("/lista")
def home():
    return "lista de usuários"

@app.route("/cadastro")
def cadastro():
    return "cadastrar usuários"

def adicionar_usuario(nome, email):
    novo_usuario = Usuario(nome=nome, email=email)
    db.session.add(novo_usuario)
    db.session.commit()

    return f"Usuário {nome} adicionado com sucesso!"  
    return f"Usuário {email} adicionado com sucesso!"   
    return f"Usuário {nome} e {email} adicionado com sucesso!" 
    return redirect(url_for('home'))

@app.route("/adicionar_usuario/<nome>/<email>")
def adicionar_usuario_route(nome, email):
    return adicionar_usuario(nome, email)

@app.route("/usuarios")
def listar_usuarios():
    usuarios = Usuario.query.all()
    return "<br>".join([f"{usuario.nome} - {usuario.email}" for usuario in usuarios])

if __name__ == "__main__":  app.run(debug=True)


