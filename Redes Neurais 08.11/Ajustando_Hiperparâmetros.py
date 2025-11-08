# ==============================================
# TESTE DE TAXAS DE APRENDIZADO (Learning Rate)
# ==============================================
# Este código treina várias vezes uma rede neural simples
# mudando apenas a "taxa de aprendizado" (learning rate).
# O objetivo é mostrar como esse parâmetro afeta a precisão
# do modelo durante o treinamento.
# ----------------------------------------------
# Requisitos: TensorFlow e scikit-learn (já devem ter sido importados antes)
# ----------------------------------------------

# A estrutura básica da rede é a mesma usada no exemplo anterior:
# - Camada oculta com 8 neurônios
# - Camada de saída com 3 neurônios (3 classes do conjunto Iris)
# - Função de ativação ReLU na camada oculta e Softmax na saída

# Vamos repetir o processo para três valores de taxa de aprendizado (lr):
# 0.01, 0.001 e 0.0001
# Cada valor controla o "tamanho do passo" de ajuste dos pesos
# durante o aprendizado da rede.

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input # Importar Input

# Loop para testar diferentes taxas de aprendizado
for lr in [0.01, 0.001, 0.0001]:
    # === Criação da rede ===
    model = Sequential([
        Input(shape=(4,)),  # Adiciona a camada Input como recomendado
        Dense(8, activation='relu'),  # 1ª camada oculta (8 neurônios)
        Dense(3, activation='softmax')                  # Camada de saída (3 neurônios → 3 classes)
    ])

    # === Compilação do modelo ===
    # - Otimizador "adam": método automático que ajusta a taxa de aprendizado internamente
    # - Função de perda: categorical_crossentropy (usada para classificação com várias classes)
    # - Métrica: accuracy (porcentagem de acertos)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # === Ajuste manual da taxa de aprendizado ===
    # Aqui, forçamos o modelo a usar a taxa de aprendizado definida na variável "lr".
    model.optimizer.learning_rate = lr

    # === Treinamento do modelo ===
    # - epochs: número de vezes que o modelo “vê” todos os dados de treino
    # - verbose=0: não exibe mensagens de progresso
    model.fit(X_train, y_train, epochs=30, verbose=0)

    # === Avaliação do modelo ===
    # Testa o modelo nos dados de teste e obtém a acurácia
    _, acc = model.evaluate(X_test, y_test, verbose=0)

    # Exibe os resultados formatados
    print(f"Learning Rate={lr} → Acurácia={acc:.3f}")

'''
========================================================
EXPLICAÇÃO:

Taxa de aprendizado (Learning Rate):
- Controla o tamanho dos passos que o modelo dá ao ajustar seus pesos.
- Taxas muito grandes → o modelo pode “saltar” o ponto ideal e não convergir.
- Taxas muito pequenas → o aprendizado é muito lento.

Outros parâmetros importantes que afetam o desempenho da rede:

1 - Número de camadas ocultas e neurônios:
   - Mais camadas → mais capacidade de aprender padrões complexos.
   - Porém, aumenta o risco de sobreajuste (overfitting).

2 - Funções de ativação:
   - relu → boa para camadas intermediárias.
   - sigmoid / tanh → usadas em redes menores ou de saída binária.

3 - Otimizadores:
   - adam → mais usado (autoajuste da taxa de aprendizado).
   - sgd → gradiente descendente clássico.
   - rmsprop → bom para séries temporais.

4 - Regularização:
   - dropout → “desliga” neurônios aleatórios durante o treino.
   - early stopping → interrompe o treino quando o modelo para de melhorar.
========================================================
'''