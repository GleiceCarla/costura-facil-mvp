
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    """Exibe a página inicial do Costura Fácil."""
    return render_template("index.html")


@app.route("/novo-pedido", methods=["GET"])
def novo_pedido():
    return render_template("novo_pedido.html")


if __name__ == "__main__":
    app.run(debug=False)
