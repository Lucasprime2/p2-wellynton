import os

script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
livros_path = os.path.join(script_dir, 'livros.txt')
saida_path = os.path.join(script_dir, 'livros_avaliacao.txt')

def ler_nota(prompt):
    while True:
        entrada = input(prompt).strip().replace(',', '.')
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                return nota
            else:
                print("Erro: A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: Digite um número válido.")

def ler_status(prompt):
    while True:
        status = input(prompt).strip().lower()
        if status in ["lido", "lendo", "na fila"]:
            return status
        print('Erro: Status deve ser "lido", "lendo" ou "na fila".')

if not os.path.exists(livros_path):
    print("Arquivo de livros não encontrado em:", livros_path)
    raise SystemExit

with open(livros_path, 'r', encoding='utf-8') as f:
    livros = [linha.strip() for linha in f if linha.strip()]

if not livros:
    print("Nenhum registro encontrado em", livros_path)
    raise SystemExit

avaliacoes = []
print("Digite as avaliações para os livros:")
for livro in livros:
    partes = livro.split(', ', 2)
    titulo = partes[1] if len(partes) > 1 else livro
    nota = ler_nota(f"Nota para '{titulo}' (0-10): ")
    status = ler_status(f"Status para '{titulo}' (lido/lendo/na fila): ")
    avaliacoes.append(f"{livro}, {nota}, {status}")

with open(saida_path, 'w', encoding='utf-8') as f:
    for linha in avaliacoes:
        f.write(linha + '\n')

print("\nArquivo de avaliações criado em:", saida_path)
print("Conteúdo gravado:")
with open(saida_path, 'r', encoding='utf-8') as f:
    print(f.read())