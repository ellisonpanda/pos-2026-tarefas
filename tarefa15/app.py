from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return "Página de Login"


@app.route("/callback")
def callback():
    return "Callback"


@app.route("/perfil")
def perfil():
    return "Perfil"


@app.route("/boletim")
def boletim():
    return "Boletim"


@app.route("/logout")
def logout():
    return "Logout"


if __name__ == "__main__":
    app.run(debug=True)