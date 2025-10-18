# Instalar (caso necessário): pip install owlready2

from owlready2 import *

# Criamos uma nova ontologia
onto = get_ontology("http://exemplo.org/educacao.owl")

with onto:
    # Definindo classes (conceitos)
    class Pessoa(Thing): pass
    class Professor(Pessoa): pass
    class Aluno(Pessoa): pass
    class Disciplina(Thing): pass

    # Definindo propriedades (relações)
    class Ensina(ObjectProperty): pass
    class Estuda(ObjectProperty): pass

# Criamos instâncias (indivíduos)
prof = Professor("Carlos")
aluno = Aluno("Ana")
disciplina = Disciplina("Inteligencia_Artificial")

# Relacionando instâncias
prof.Ensina.append(disciplina)
aluno.Estuda.append(disciplina)

# Mostrando os relacionamentos
print(f"{prof.name} ensina {prof.Ensina[0].name}")
print(f"{aluno.name} estuda {aluno.Estuda[0].name}")

'''
Comentário:

Cada classe é um conceito abstrato.

Cada instância é um exemplo real desse conceito.

As relações (propriedades) conectam conceitos entre si.
'''