import os

script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
entrada_path = os.path.join(script_dir, 'livros_avaliacao.txt')   
saida_path = os.path.join(script_dir, 'livros_recomendados.txt')    

if not os.path.exists(entrada_path):
    print("Arquivo livros_avaliacao.txt não encontrado em:", entrada_path)
    raise SystemExit


registros = []
with open(entrada_path, 'r', encoding='utf-8') as f:
    for i, linha in enumerate(f):
        linha = linha.strip()
        if not linha:
            continue
        if i == 0 and linha.lower().startswith('livro'):
            continue
        partes = linha.split(';')
        if len(partes) < 3:
            print("Linha em formato errado:", linha)
            continue
        livro = partes[0].strip()
        nota_str = partes[1].strip()
        status = partes[2].strip()
        try:
            nota = float(nota_str)
        except ValueError:
            print("Nota inválida na linha:", linha)
            continue

        if ',' in livro:
            _, titulo = livro.split(',', 1)
            titulo = titulo.strip()
        else:
            if status== "lido" or status== "lendo":
                titulo = livro
                registros.append((livro, nota, status, titulo.lower()))

if not registros:
    print("Nenhum registro válido encontrado em", entrada_path)
    raise SystemExit

def chave_registro(item):
    livro, nota, status, titulo_lower = item
    return (-nota, status, titulo_lower)
registros_ordenados = sorted(registros, key=chave_registro)
top5 = registros_ordenados[:5]

with open(saida_path, 'w', encoding='utf-8') as f:
    f.write("filme;nota;status\n")
    for filme, nota, _ in top5:
        f.write(f"{filme};{nota}\n")

print("Arquivo de indicação criado em:", saida_path)
print("Conteúdo gravado:")
with open(saida_path, 'r', encoding='utf-8') as f:
    print(f.read())