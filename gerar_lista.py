import os
import json

# Configurações
pasta_musicas = 'musicas'
artista_padrao = 'Ricardo Capel'  # Seu nome artístico
caminho_relativo = 'musicas/'     # Como o HTML vai enxergar a pasta

lista_de_musicas = []

# 1. Verifica se a pasta existe para evitar erros
if os.path.exists(pasta_musicas):
    # 2. Varre todos os arquivos da pasta
    arquivos = os.listdir(pasta_musicas)
    
    for arquivo in arquivos:
        # 3. Filtra apenas arquivos .mp3
        if arquivo.lower().endswith('.mp3'):
            
            # 4. Limpeza do nome (tira o .mp3 e troca _ por espaço)
            titulo_tratado = arquivo.replace('.mp3', '').replace('_', ' ').title()
            
            # 5. Monta o objeto da música
            musica = {
                "title": titulo_tratado,
                "artist": artista_padrao,
                "src": f"{caminho_relativo}{arquivo}",
                "cover": ""  # Se tiver capa, pode automatizar aqui também
            }
            
            lista_de_musicas.append(musica)

    # 6. Gera o JSON formatado para JavaScript
    print("--- COPIE O CÓDIGO ABAIXO E COLE NO SEU HTML ---")
    print(f"const songs = {json.dumps(lista_de_musicas, indent=4, ensure_ascii=False)};")
    print("------------------------------------------------")

else:
    print(f"Erro: A pasta '{pasta_musicas}' não foi encontrada.")