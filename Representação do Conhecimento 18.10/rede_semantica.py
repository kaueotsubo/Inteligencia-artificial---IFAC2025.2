import networkx as nx

#1. Classe principal da rede semântica
class RedeSemantica:

    #inicializa a rede semântica
    def __init__(self):
        self.grafo = nx.DiGraph()
        self.regras = []

    #Adicionar e inicializa conceitos
    def inicializar_conceitos (self, nome):
        #Adicionar um novo conceito (nó) à rede
        self.grafo.add_node(nome)

    #Adiciona relações
    def adicionar_relacao (self, origem, destino, relacao):
        #Criar uma aresta com rótulo semântico
        self.grafo.add_edge(origem, destino, relation=relacao)
        
    #Lista relações
    def listar_relacoes (self):
        for u, v, d in self.grafo.edges(data=True):
            print(f"{u}--{d['relation']} --> {v}")

    #Adiciona as regras
    def adicionar_regra (self, condicoes, conclusao):
        #Adicionar uma regra para uso na inferência
        self.regras.append((condicoes, conclusao))

    #Realiza inferência
    def inferir(self):
        novas_relacoes = []
        for condicoes, conclusao in self.regras:
            if all(self.existe_relacao(*c) for c in condicoes):
                if not self._existe_relacao(*conclusao):
                    self.adicionar_relacao(*conclusao)
                    novas_relacoes.append(conclusao)
        return novas_relacoes #novas relações conclusivas

    #Verifica se uma relação já existe
    def _existe_relacao (self, origem, destino, relacao):
        return (origem, destino) in self.grafo.edges() and \
               self.grafo[origem][destino]['relation'] == relacao
        
#2. Base de regras lógicas
def carregar_regras():
    #Conjunto de regras lógicas
    return  [
        
                (

                    [
                        ("Pessoa", "Cachorro", "possui"), ("Cachorro", "Animal", "é_um")
                    ]

                )

            ]

#3. Função de visualização gráfica
def exibir_grafo(grafo, titulo="Rede Semântica"):
    

#4. Execução principal - main()
if __name__ == "__main_":
    #inicializar a rede
    rede = RedeSemantica()
