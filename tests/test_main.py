import pytest
import json
from main import encontrar_duplicados
#...
def test_encontrar_duplicados():
    # Dados de teste:
    dados_teste = {
        "data": [
            {"id": 1, "nome": "Alice"},
            {"id": 2, "nome": "Bob"},
            {"id": 3, "nome": "Alice"},
            {"id": 4, "nome": "Charlie"},
            {"id": 5, "nome": "Bob"} 
        ]
    }

    # Resultado esperado:
    resultado_esperado = {
        "Alice": [
            {"id": 1, "nome": "Alice"},
            {"id": 3, "nome": "Alice"}
        ],
        "Bob": [
            {"id": 2, "nome": "Bob"},
            {"id": 5, "nome": "Bob"}
        ]
    }


    # Execução da função:
    duplicados = encontrar_duplicados(dados_teste["data"], "nome")

    # Verificações (asserções):
    assert duplicados == resultado_esperado
#...
def test_arquivo_json_inexistente():
    with pytest.raises(FileNotFoundError):
        with open("teste.json", "r") as arquivo_json:
            dados = json.load(arquivo_json)

def test_chave_inexistente():
    dados_teste = {
        "data": [
            {"id": 1, "nome": "Alice"},
            {"id": 2, "nome": "Bob"}
        ]
    }

    duplicados = encontrar_duplicados(dados_teste["data"], "chave_inexistente")
    assert duplicados == {}  # Não deve haver duplicados para uma chave inexistente
