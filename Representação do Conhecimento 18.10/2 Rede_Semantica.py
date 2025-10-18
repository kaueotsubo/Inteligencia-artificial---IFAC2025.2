# Atualizar pip install --upgrade --force-reinstall numpy
# Instalar (caso necessário): pip install networkx matplotlib

import networkx as nx
import matplotlib.pyplot as plt

# Criamos um grafo direcionado
G = nx.DiGraph()

# Adicionamos nós e as relações (arestas)
G.add_edge("Gato", "Animal", relation="é um")
G.add_edge("Animal", "Coração", relation="tem")
G.add_edge("Gato", "Leite", relation="bebe")

# Exibimos as relações em texto
for u, v, d in G.edges(data=True):
    print(f"{u} —{d['relation']}→ {v}")

# Exibimos graficamente a rede
plt.figure(figsize=(6, 4))
nx.draw(G, with_labels=True, node_color='lightgreen', node_size=2500, font_size=10, arrows=True)
plt.show()

'''
Comentário:

Cada nó é um conceito (ex: “Gato”).

Cada aresta é uma relação (ex: “é um”, “bebe”).

A visualização ajuda a compreender a estrutura semântica do conhecimento.

'''