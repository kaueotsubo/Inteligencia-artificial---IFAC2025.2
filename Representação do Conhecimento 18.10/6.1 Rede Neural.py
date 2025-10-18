# Exemplo: Rede Neural Perceptron para aprender a função lógica AND
# Autor: exemplo didático de representação do conhecimento por redes neurais

import numpy as np

# -----------------------------
# 1. Conjunto de treinamento
# -----------------------------
# Entradas (X): todas as combinações de 0 e 1
# Saídas esperadas (y): resultado da função lógica AND
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0],   # 0 AND 0 = 0
              [0],   # 0 AND 1 = 0
              [0],   # 1 AND 0 = 0
              [1]])  # 1 AND 1 = 1


# -----------------------------
# 2. Inicialização dos pesos
# -----------------------------
np.random.seed(42)
pesos = np.random.rand(2, 1)  # 2 entradas -> 1 saída
taxa_aprendizado = 0.1

# Função de ativação: degrau (step)
def ativacao(x):
    return np.where(x >= 0.5, 1, 0)

# -----------------------------
# 3. Processo de treinamento
# -----------------------------
for epoca in range(20):  # 20 iterações de aprendizado
    # Calcula a saída da rede
    entrada_liquida = np.dot(X, pesos)
    saida = ativacao(entrada_liquida)
    
    # Calcula o erro
    erro = y - saida
    
    # Atualiza os pesos (regra do perceptron)
    pesos += taxa_aprendizado * np.dot(X.T, erro)
    
    print(f"Época {epoca+1}: Erro total = {np.sum(np.abs(erro))}")

# -----------------------------
# 4. Teste da rede
# -----------------------------
print("\nPesos finais aprendidos:")
print(pesos)

print("\nTestando a rede:")
for entrada in X:
    resultado = ativacao(np.dot(entrada, pesos))
    print(f"{entrada} -> {resultado}")
