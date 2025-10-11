# Instalar (caso necessário): pip install scikit-learn

from sklearn.neural_network import MLPClassifier

# Dados de treinamento: [altura (m), peso (kg)]
X = [[1.70, 65], [1.60, 50], [1.80, 80], [1.55, 45]]
y = ["Homem", "Mulher", "Homem", "Mulher"]

# Criando e treinando a rede neural
modelo = MLPClassifier(max_iter=1000)
modelo.fit(X, y)

# Fazendo uma previsão
novo_exemplo = [[1.75, 70]]
print("Predição:", modelo.predict(novo_exemplo)[0])
