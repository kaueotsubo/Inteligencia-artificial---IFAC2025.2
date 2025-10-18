# Importação das bibliotecas necessárias
import networkx as nx
import matplotlib.pyplot as plt

# Criação de um grafo direcionado (relações têm sentido)
G = nx.DiGraph()

# Adiciona os nós (conceitos)
G.add_nodes_from(["Cachorro", "Pessoa", "Casa"])

# Adiciona as arestas (relações entre os conceitos)
G.add_edge("Cachorro", "Pessoa", relation="pertence_a")
G.add_edge("Pessoa", "Casa", relation="mora_em")

# Define a posição dos nós para melhor visualização
pos = nx.spring_layout(G, seed=1)

# Desenha os nós
nx.draw(
    G, pos,
    with_labels=True,
    node_color="lightblue",
    node_size=2500,
    font_size=10,
    font_weight="bold",
    arrows=True
)

# Adiciona os rótulos das relações nas arestas
edge_labels = nx.get_edge_attributes(G, 'relation')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

# Título do gráfico
plt.title("Rede Semântica: 'Um cachorro pertence a uma pessoa e essa pessoa mora em uma casa'")
plt.show()
