# Importa o numpy
import numpy as np

# Cria a função calulate e define seu parâmetro
def calculate(list):
    if len(list) !=9:
        raise ValueError("List must contain nine numbers.")
    
    # Transforma a lista passada como parâmetro em uma matriz 3x3
    matriz = np.array(list).reshape(3, 3)

    # Cria o dicionário que faz os cálculos necessários
    calculations = {
        'mean': [matriz.mean(axis= 0).tolist(), matriz.mean(axis = 1).tolist(), float(matriz.mean())],
        'variance': [matriz.var(axis= 0).tolist(), matriz.var(axis= 1).tolist(), float(matriz.var())],
        'standard deviation': [matriz.std(axis= 0).tolist(), matriz.std(axis = 1).tolist(), float(matriz.std())],
        'max': [matriz.max(axis= 0).tolist(), matriz.max(axis= 1).tolist(), float(matriz.max())],
        'min': [matriz.min(axis= 0).tolist(), matriz.min(axis= 1).tolist(), float(matriz.min())],
        'sum': [matriz.sum(axis= 0).tolist(), matriz.sum(axis= 1).tolist(), float(matriz.sum())]
    }

    # Retorna os resultaodos dos objetos armazenados no dicionário
    return calculations