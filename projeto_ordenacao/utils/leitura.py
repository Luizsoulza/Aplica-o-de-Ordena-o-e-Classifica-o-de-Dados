import pandas as pd
from pathlib import Path

def carregar_pontos(caminho_arquivo: str):
    """Lê um arquivo CSV e devolve a lista de pontos (coluna 'Pontos').

    caminho_arquivo: caminho para o arquivo CSV.
    retorna: lista de inteiros ou floats com os pontos.
    """
    caminho = Path(caminho_arquivo)

    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

    dados = pd.read_csv(caminho)
    
    if "Pontos" not in dados.columns:
        raise ValueError("A coluna 'Pontos' não existe no arquivo CSV.")

    pontos = dados["Pontos"].tolist()
    return pontos
