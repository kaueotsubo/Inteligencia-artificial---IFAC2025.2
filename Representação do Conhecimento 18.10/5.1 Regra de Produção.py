# Exemplo de Representação do Conhecimento por Regras de Produção
# Tema: Sistema especialista para diagnóstico de clima

# Cada regra segue a estrutura:
# SE <condição> ENTÃO <ação>

class SistemaEspecialista:
    def __init__(self):
        self.regras = []
    
    def adicionar_regra(self, condicao, acao):
        """Adiciona uma regra SE ... ENTÃO ..."""
        self.regras.append({"condicao": condicao, "acao": acao})
    
    def inferir(self, fatos):
        """Aplica as regras sobre os fatos conhecidos"""
        acoes_disparadas = []
        for regra in self.regras:
            # Avalia se a condição é verdadeira com base nos fatos conhecidos
            if regra["condicao"](fatos):
                acoes_disparadas.append(regra["acao"])
        return acoes_disparadas


# --- Exemplo de uso do sistema ---

# 1. Criamos o sistema
sistema = SistemaEspecialista()

# 2. Adicionamos regras de produção
sistema.adicionar_regra(
    lambda f: f.get("chuva") == True,
    "Leve um guarda-chuva."
)

sistema.adicionar_regra(
    lambda f: f.get("temperatura", 0) > 30,
    "Use roupas leves e protetor solar."
)

sistema.adicionar_regra(
    lambda f: f.get("vento") == True and f.get("chuva") == False,
    "Evite lugares abertos, está ventando muito."
)

sistema.adicionar_regra(
    lambda f: f.get("chuva") == False and f.get("temperatura", 0) < 20,
    "Use um agasalho, o tempo está frio e seco."
)

# 3. Fatos (informações conhecidas)
fatos = {
    "chuva": False,
    "vento": True,
    "temperatura": 18
}

# 4. Motor de inferência executa as regras
acoes = sistema.inferir(fatos)

# 5. Exibe o resultado
print("Condições atuais:", fatos)
print("\nRecomendações:")
for acao in acoes:
    print("-", acao)
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
