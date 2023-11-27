import cv2
import csv
import os

def processa_frames(frames_folder):
    # Lista todos os arquivos no diretório dos frames
    frames = [f for f in os.listdir(frames_folder) if f.endswith('.png') or f.endswith('.jpg')]

    # Ordena os frames com base nos números nos nomes dos arquivos
    frames.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

    # Dicionário para armazenar os resultados
    resultados = {}

    # Lista de métodos na ordem desejada
    metodos = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    # Loop pelos métodos
    for i, metodo in enumerate(metodos):
        resultados[metodo] = []

        print(f"\nAnalisando com o método {i} ({metodo}):\n")

        # Loop pelos quadros
        for frame in frames:
            print(f"Analisando o quadro: {frame}")
            
            # Carrega a imagem do quadro
            imagem = cv2.imread(os.path.join(frames_folder, frame))

            # Carrega a imagem do template (pode ser ajustada conforme necessário)
            template = cv2.imread("template.PNG")

            # Aplica o método
            result = cv2.matchTemplate(imagem, template, metodo)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            # Armazena os resultados
            resultados[metodo].append({'Quadro': frame, 'min_val': min_val, 'max_val': max_val})

    return resultados

def salva_resultados_csv(resultados, output_folder):
    for metodo, dados in resultados.items():
        output_file = os.path.join(output_folder, f'tabela_{metodo}.csv')
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = ['Quadro', 'min_val', 'max_val']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Escreve o cabeçalho
            writer.writeheader()

            # Escreve os dados
            for linha in dados:
                writer.writerow(linha)

if __name__ == "__main__":
    # Especifica o diretório dos frames
    frames_folder = "./frames"

    # Especifica o diretório de saída para os arquivos CSV
    output_folder = "./output/tabelas"

    # Processa os frames e obtém os resultados
    resultados = processa_frames(frames_folder)

    # Salva os resultados em arquivos CSV
    salva_resultados_csv(resultados, output_folder)
