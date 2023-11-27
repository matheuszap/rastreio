import os

diretorio_frames = "./frames"

# Verifica se o diretório existe
if not os.path.exists(diretorio_frames):
    print("O diretório não existe. Verifique o caminho fornecido.")
else:
    # Obtém a lista de arquivos no diretório
    arquivos = os.listdir(diretorio_frames)

    # Filtra apenas os arquivos .png
    arquivos_png = [arquivo for arquivo in arquivos if arquivo.endswith(".png")]

    # Ordena os arquivos em ordem crescente
    arquivos_png.sort()

    # Renomeia os arquivos
    for indice, arquivo in enumerate(arquivos_png, start=1):
        antigo_caminho = os.path.join(diretorio_frames, arquivo)
        novo_nome = f"{indice}.png"
        novo_caminho = os.path.join(diretorio_frames, novo_nome)

        # Renomeia o arquivo
        os.rename(antigo_caminho, novo_caminho)

        print(f"Renomeado: {arquivo} para {novo_nome}")

print("Concluído.")
