# ==========================================
# RECONHECIMENTO DE PADRÕES COM REDE NEURAL
# ==========================================
# Este código demonstra o uso básico de uma Rede Neural Artificial (RNA)
# utilizando o TensorFlow e Keras.
# Ele treina o modelo para aprender um padrão simples a partir de dados
# de entrada e prever resultados com base nesse aprendizado.
# ------------------------------------------
# Autor: [Seu nome]
# Ambiente sugerido: Google Colab
# ------------------------------------------

# ======== IMPORTAÇÃO DAS BIBLIOTECAS ========
# O TensorFlow é uma biblioteca de código aberto desenvolvida pelo Google
# para criação e treinamento de modelos de Inteligência Artificial (IA).
# Ele contém ferramentas para aprendizado de máquina, redes neurais,
# processamento de imagens, voz, texto e muito mais.
import tensorflow as tf

# O NumPy é uma biblioteca para cálculos matemáticos e manipulação de matrizes.
# É amplamente usada em projetos científicos e de IA.
import numpy as np


# ======== GERAÇÃO DE DADOS DE EXEMPLO ========
# Aqui criamos dados simples apenas para demonstrar o funcionamento.
# Entrada (x): números de 1 a 10
# Saída (y): o dobro de cada número de x
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], dtype=float)


# ======== CONSTRUÇÃO DO MODELO ========
# O modelo é construído de forma sequencial (camada sobre camada).
# Cada camada possui "neurônios", e cada neurônio processa informações.
# O modelo abaixo possui:
# - Uma camada densa (fully connected) com 1 neurônio e uma entrada de 1 dimensão.
# Essa camada aprenderá a relação entre x e y (no caso, a multiplicação por 2).
modelo = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),  # Define o formato da entrada (1 valor por vez)
    tf.keras.layers.Dense(1)            # Camada densa com 1 neurônio de saída
])


# ======== COMPILAÇÃO DO MODELO ========
# Aqui definimos como o modelo "aprende":
# - optimizer: método que ajusta os pesos da rede para reduzir o erro
#   'adam' é um otimizador popular e eficiente.
# - loss: função de erro (mede o quanto o modelo erra nas previsões)
#   'mean_squared_error' é o erro quadrático médio.
modelo.compile(optimizer='adam', loss='mean_squared_error')


# ======== TREINAMENTO DO MODELO ========
# O modelo treina observando os dados várias vezes (épocas).
# Cada época é uma passagem completa pelos dados de treinamento.
# Quanto mais épocas, mais o modelo aprende — mas cuidado com o "overfitting".
print("Treinando o modelo...\n")
historico = modelo.fit(x, y, epochs=5000, verbose=0)  # Aumentando as épocas para melhor aprendizado


# ======== TESTE DO MODELO ========
# Após o treinamento, testamos o modelo com novos dados.
# O modelo deve prever aproximadamente o dobro do valor fornecido.
valor_teste = 11.0
resultado = modelo.predict(np.array([valor_teste])) # Convertendo para array NumPy

print(f"O modelo prevê que o dobro de {valor_teste} é aproximadamente {resultado[0][0]:.2f}")


# ======== VISUALIZAÇÃO DO APRENDIZADO ========
# Exibimos a curva de aprendizado (redução do erro ao longo das épocas).
# Isso ajuda a entender se o modelo realmente aprendeu ou ainda precisa de ajustes.
import matplotlib.pyplot as plt

plt.plot(historico.history['loss'])
plt.title('Evolução do Erro Durante o Treinamento')
plt.xlabel('Época')
plt.ylabel('Erro Quadrático Médio (Loss)')
plt.show()