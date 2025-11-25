import os
script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
entrada_path = os.path.join(script_dir, 'livros_recomendados.txt')

if not os.path.exists(entrada_path):
    print("Arquivo livros_recomendados.txt não encontrado em:", entrada_path)
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
        if len(partes) < 2:
            continue
        livro = partes[0].strip()
        nota_str = partes[1].strip()
       
        try:
            nota = float(nota_str)
        except ValueError:
            continue
        if ',' in livro:
            _, titulo = livro.split(',', 1)
            titulo = titulo.strip()
        else:
            titulo = livro
        registros.append((livro, nota, titulo.lower()))

if not registros:
    print("Nenhum registro válido em", entrada_path)
    raise SystemExit

def chave_ordem(item):
    return (-item[1], item[2])

registros_ordenados = sorted(registros, key=chave_ordem)

print("Livros da maior para a menor nota:")
for idx, (livro, nota, _) in enumerate(registros_ordenados, start=1):
    print(f"{idx}. {livro}  -  nota: {nota:g}")