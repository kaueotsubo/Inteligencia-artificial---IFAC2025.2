# Importa as bibliotecas necessárias
# networkx -> para criar e manipular grafos (redes semânticas)
# matplotlib -> para desenhar o grafo na tela
import networkx as nx
import matplotlib.pyplot as plt

# Criação de um grafo direcionado (as relações têm direção)
G = nx.DiGraph()

# Adiciona os nós (conceitos principais da frase)
G.add_nodes_from(["Estudante", "Escola", "Livro", "Estudar", "Ler"])

# Adiciona as arestas (relações entre os conceitos)
# Cada aresta é uma ligação entre dois nós, com um "rótulo" (nome da relação)
G.add_edge("Estudante", "Escola", relation="estuda em")   # O estudante estuda em uma escola
G.add_edge("Estudante", "Livro", relation="lê")           # O estudante lê livros
G.add_edge("Estudar", "Escola", relation="ocorre em")     # O ato de estudar ocorre na escola
G.add_edge("Ler", "Livro", relation="tem objeto")         # O ato de ler tem como objeto o livro

# Define a posição dos nós no gráfico
# (spring_layout tenta organizar o grafo de forma visualmente equilibrada)
pos = nx.spring_layout(G, seed=42)

# Desenha os nós e as setas (arestas)
nx.draw(
    G, pos, 
    with_labels=True,        # Mostra os nomes dos nós
    node_color='lightgreen', # Cor dos nós
    node_size=2500,          # Tamanho dos nós
    font_size=10,            # Tamanho do texto dos nós
    font_weight='bold',      # Negrito nos rótulos dos nós
    arrows=True              # Mostra as setas indicando a direção das relações
)

# Obtém os rótulos das arestas (nomes das relações)
edge_labels = nx.get_edge_attributes(G, 'relation')

# Desenha os rótulos das relações (arestas)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

# Adiciona um título ao gráfico
plt.title("Rede Semântica: 'Um estudante estuda em uma escola e lê livros'")

# Exibe o grafo
plt.show()
