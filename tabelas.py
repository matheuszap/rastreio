import os
import pandas as pd
import matplotlib.pyplot as plt

def carrega_tabela_csv(caminho_arquivo):
    tabela = pd.read_csv(caminho_arquivo)
    return tabela

def cria_grafico(tabela, metodo, output_folder):
    fig, ax = plt.subplots()
    
    ax.plot(tabela['Quadro'], tabela['min_val'], label='min_val')
    ax.plot(tabela['Quadro'], tabela['max_val'], label='max_val')

    ax.set_xlabel('Imagens')
    ax.set_ylabel('Valor')
    ax.set_title(f'Método: {metodo}')

    # Adiciona ticks (marcadores) a cada 10 quadros
    ax.set_xticks(tabela['Quadro'][::25])

    ax.legend()

    # Cria o diretório 'graficos' se ainda não existir
    os.makedirs(output_folder, exist_ok=True)

    # Salva o gráfico no diretório 'graficos' com o nome baseado no método
    nome_arquivo = os.path.join(output_folder, f'grafico_{metodo.replace(".", "_")}.png')
    plt.savefig(nome_arquivo)
    plt.close()

if __name__ == "__main__":
    # Especifica o diretório de saída para os arquivos CSV
    output_folder = "./output"

    # Especifica o diretório para os gráficos
    graficos_folder = os.path.join(output_folder, "graficos")

    # Nomes dos métodos na ordem correta
    nomes_metodos = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

    # Loop pelos métodos
    for i, nome_metodo in enumerate(nomes_metodos):
        # Constrói o nome do arquivo
        caminho_arquivo = os.path.join(output_folder, f'tabela_{i}.csv')

        # Carrega a tabela correspondente ao método
        tabela = carrega_tabela_csv(caminho_arquivo)

        # Cria o gráfico e salva no diretório 'graficos'
        cria_grafico(tabela, nome_metodo, graficos_folder)
