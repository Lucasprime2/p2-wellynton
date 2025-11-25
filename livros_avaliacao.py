import os
script_dir = os.path.dirname(os.path.abspath(__file__)) if '__file__' in globals() else os.getcwd()
livros_path = os.path.join(script_dir, 'livros.txt')                    
saida_path = os.path.join(script_dir, 'livros_avaliacao.txt')           

def ler_nota(prompt):
    while True:
        s = input(prompt).strip()
        s = s.replace(',', '.')        
        try:
            nota = float(s)
        except ValueError:
            print("Erro: digite um número 0-10.")
            continue
        if 0 <= nota <= 10:
            return nota
        else:
            print("Erro: Digite um número 0-10.")

def ler_status(prompt2):
   while True:
        
        x = input(prompt2).strip()
        if x != "lido" and x!= "lendo" and x!= "na fila":
            print("Digite o status correto: lido, lendo ou na fila")
            continue
        elif x== "lido" or x== "lendo" or x == "na fila":
            return x
        else:
            print("Erro: Digite um status correto (lido, lendo ou na fila)")


if not os.path.exists(livros_path):
    print("Arquivo de livros não encontrado em:", livros_path)
    raise SystemExit

livros = []
with open(livros_path, 'r', encoding='utf-8') as f:
    for linha in f:
        linha = linha.strip()
        if not linha:
            continue
        livros.append(linha)

if not livros:
    print("Nenhum registro encontrado em", livros_path)
    raise SystemExit

avaliacoes = []
print("Digite as notas para os livros:")
for registro in livros:
 
    if ',' in registro:
        _, titulo = registro.split(',', 1)
        titulo = titulo.strip()
    else:
        titulo = registro
    prompt = f"Nota para '{titulo}': "
    prompt2 = f"Status para '{titulo} - lido, lendo ou na fila: "
    nota = ler_nota(prompt)
    status = ler_status(prompt2)
    avaliacoes.append((registro, nota, status))

with open(saida_path, 'w', encoding='utf-8') as f:
    f.write("livro;nota;status\n")   
    for reg, nota, status in avaliacoes:
        f.write(f"{reg};{nota};{status}\n")

print("\nArquivo de avaliações criado em:", saida_path)
print("Conteúdo gravado:")
with open(saida_path, 'r', encoding='utf-8') as f:
    print(f.read())