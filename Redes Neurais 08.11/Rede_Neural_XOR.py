# ==========================================
# REDE NEURAL SIMPLES EM PYTHON - Introdução
# ==========================================
# Este código mostra como uma rede neural simples pode aprender o problema lógico XOR.
# Ele foi feito apenas com a biblioteca NumPy, sem usar nenhuma ferramenta de IA pronta.
# Assim, você vê passo a passo como o computador "aprende" por meio de ajustes de números.

# ------------------------------------------
# Importando a biblioteca NumPy
# ------------------------------------------
# O NumPy é uma biblioteca do Python que facilita o trabalho com cálculos numéricos,
# especialmente com vetores e matrizes (listas de números organizadas em linhas e colunas).
import numpy as np

# ------------------------------------------
# Conjunto de dados (entradas e saídas esperadas)
# ------------------------------------------
# Aqui definimos as combinações de entrada (X) e a saída correta (y) para o problema XOR.
# XOR (OU EXCLUSIVO) é uma operação lógica:
# - 0 XOR 0 → 0
# - 0 XOR 1 → 1
# - 1 XOR 0 → 1
# - 1 XOR 1 → 0
# A rede precisará "descobrir" essa regra sozinha.
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])  # Saídas esperadas

# ------------------------------------------
# Inicialização aleatória dos pesos e bias
# ------------------------------------------
# Os "pesos" (W1 e W2) são números que a rede ajusta para aprender.
# O "bias" (b1 e b2) é um valor adicional que ajuda o neurônio a se ajustar melhor.
# A função np.random.seed(42) garante que os números aleatórios gerados sejam sempre os mesmos,
# o que facilita a reprodução dos resultados (útil para testes).
np.random.seed(42)
W1 = np.random.randn(2, 3)  # 2 neurônios de entrada → 3 neurônios na camada intermediária (oculta)
b1 = np.zeros((1, 3))       # Bias da camada oculta (3 valores)
W2 = np.random.randn(3, 1)  # 3 neurônios ocultos → 1 neurônio de saída
b2 = np.zeros((1, 1))       # Bias da camada de saída

# ------------------------------------------
# Função de ativação: Sigmoid
# ------------------------------------------
# A função sigmoid transforma qualquer número em um valor entre 0 e 1.
# Isso ajuda a rede a lidar com resultados "suavizados" em vez de 0 e 1 fixos.
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# A derivada da sigmoid serve para calcular o quanto o erro de um neurônio
# deve influenciar a atualização dos pesos (usada na retropropagação).
def sigmoid_deriv(x):
    return x * (1 - x)

# ------------------------------------------
# Taxa de aprendizado (learning rate)
# ------------------------------------------
# Esse valor (lr) controla o "ritmo" de aprendizado da rede:
# - valores muito altos podem fazer a rede pular a resposta correta,
# - valores muito baixos fazem o aprendizado demorar.
lr = 0.1

# ------------------------------------------
# Treinamento da rede
# ------------------------------------------
# A rede será treinada por 10.000 rodadas (épocas).
# Em cada rodada, ela faz previsões, calcula o erro e ajusta seus pesos.
for epoch in range(10000):

    # === ETAPA 1: Propagação para frente (Forward propagation) ===
    # A entrada (X) passa pela camada oculta e depois pela camada de saída.
    # np.dot faz a multiplicação de matrizes: entradas × pesos.
    z1 = np.dot(X, W1) + b1   # Soma ponderada da 1ª camada
    a1 = sigmoid(z1)          # Aplica a função sigmoid na camada oculta
    z2 = np.dot(a1, W2) + b2  # Soma ponderada da 2ª camada
    a2 = sigmoid(z2)          # Resultado final da rede (saída)

    # === ETAPA 2: Cálculo do erro ===
    # Compara a saída da rede (a2) com a saída esperada (y).
    erro = y - a2

    # === ETAPA 3: Retropropagação (Backpropagation) ===
    # Aqui a rede calcula o quanto cada peso contribuiu para o erro
    # e os ajusta para reduzir o erro nas próximas iterações.

    # Calcula o "gradiente" da camada de saída:
    # quanto o erro muda com relação aos valores da saída (a2).
    d_a2 = erro * sigmoid_deriv(a2)

    # Calcula o gradiente da camada oculta:
    # usa os gradientes da camada de saída e os pesos W2 para
    # descobrir como cada neurônio da camada anterior influenciou o erro.
    d_a1 = np.dot(d_a2, W2.T) * sigmoid_deriv(a1)

    # === ETAPA 4: Atualização dos pesos e bias ===
    # Ajusta os pesos e biases usando os gradientes calculados.
    # Multiplica-se pelo fator de aprendizado (lr) para controlar o tamanho da correção.
    W2 += lr * np.dot(a1.T, d_a2)
    b2 += lr * np.sum(d_a2, axis=0, keepdims=True)
    W1 += lr * np.dot(X.T, d_a1)
    b1 += lr * np.sum(d_a1, axis=0, keepdims=True)

# ------------------------------------------
# Exibindo o resultado final
# ------------------------------------------
# Após o treinamento, a rede "aprendeu" o padrão do XOR.
# Agora imprimimos a saída final para ver se ela acertou os valores esperados.
print("Saída final da rede:")
print(a2.round(3))  # arredonda os resultados para 3 casas decimais

# ------------------------------------------
# Conclusão
# ------------------------------------------
# Esta rede neural simples aprendeu o comportamento da função XOR.
# Isso é algo que um perceptron simples (com apenas uma camada) não conseguiria fazer.
# O código mostra, na prática, como funciona o processo de aprendizado:
# 1. a rede faz uma previsão;
# 2. mede o erro;
# 3. ajusta seus pesos;
# 4. repete o processo até "aprender".
