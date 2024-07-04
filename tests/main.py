import json

#...
def encontrar_duplicados(json_data, chave):
    duplicados = {}
    for item in json_data:
        if chave in item:  # Verifica se a chave existe no item
            valor_chave = item[chave]
            if valor_chave in duplicados:
                duplicados[valor_chave].append(item)
            else:
                duplicados[valor_chave] = [item]
    return {chave: itens for chave, itens in duplicados.items() if len(itens) > 1}
#...

# Leitura do JSON
with open('teste.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)

# Encontrar duplicados com base na chave 'nome'
duplicados = encontrar_duplicados(dados['data'], 'nome')

# Escrever os duplicados em um arquivo de texto formatado
with open('duplicados.txt', 'w') as arquivo_txt:
    for chave, itens in duplicados.items():
        arquivo_txt.write(f'Duplicados para a chave "{chave}":\n')
        for item in itens:
            arquivo_txt.write(json.dumps(item, indent=4))
            arquivo_txt.write('\n\n')
