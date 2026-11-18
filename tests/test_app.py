
import pytest
from app import app


@pytest.fixture
def cliente():
    app.config["TESTING"] = True
    with app.test_client() as cliente_teste:
        yield cliente_teste


def test_pagina_inicial(cliente):
    resposta = cliente.get("/")
    assert resposta.status_code == 200
    assert "Costura Fácil" in resposta.get_data(as_text=True)


def test_pagina_novo_pedido(cliente):
    resposta = cliente.get("/novo-pedido")
    assert resposta.status_code == 200
    assert "Novo pedido" in resposta.get_data(as_text=True)


def test_pagina_inexistente(cliente):
    resposta = cliente.get("/pagina-inexistente")
    assert resposta.status_code == 404
