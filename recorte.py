import os
import shutil

# Define os caminhos das pastas de origem e destino
pasta_origem = "C:\Users\PC EXATTA\Desktop\teste_automacao\matriz"
pasta_destino = "C:\Users\PC EXATTA\Desktop\teste_automacao\destino"

# Lista dos nomes de arquivos que você deseja recortar
nomes_arquivos = ["FichaClinica", "fichaclinica", "FICHACLINICA"]

def recortar_arquivos_especificos(pasta_origem, pasta_destino, nomes_arquivos):
    # Verifica se a pasta de destino existe, se não, cria-a
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    for nome_arquivo in nomes_arquivos:
        caminho_arquivo = os.path.join(pasta_origem, nome_arquivo)
        
        # Verifica se o arquivo existe na pasta de origem
        if os.path.isfile(caminho_arquivo):
            caminho_destino = os.path.join(pasta_destino, nome_arquivo)
            
            # Realiza a operação de recorte
            shutil.move(caminho_arquivo, caminho_destino)
            print(f"Arquivo {nome_arquivo} recortado para {caminho_destino}")

recortar_arquivos_especificos(pasta_origem, pasta_destino, nomes_arquivos)