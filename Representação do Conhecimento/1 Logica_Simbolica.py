# Instalar (caso ainda não tenha): pip install kanren

from kanren import run, var, Relation, facts

# Criamos uma relação chamada "é_humano"
humano = Relation()
facts(humano, ("Socrates",), ("Platão",))

# Criamos outra relação chamada "é_mortal"
mortal = Relation()
facts(mortal, ("Socrates",))

# Agora, queremos descobrir quem é mortal
x = var()
resultado = run(0, x, mortal(x))

print("Quem é mortal:", resultado)

'''
Comentário:

Cada fato é declarado com facts().

A consulta run() busca todos os valores de x que satisfazem a condição.

Assim, o sistema “raciocina” logicamente sobre os fatos declarados.

'''
