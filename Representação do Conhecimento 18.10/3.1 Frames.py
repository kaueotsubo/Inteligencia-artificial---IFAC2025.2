# Representação de frames em redes de conhecimento

# Cada frame será representado por um dicionário Python
# Os 'slots' (atributos) terão valores que podem ser simples (texto) ou outros frames (referência a outro dicionário)

# Frame da pessoa
pessoa = {
    "tipo": "Pessoa",
    "nome": "João",
    "idade": 30,
    "endereco": "Rua das Flores, 123"
}

# Frame do cachorro
cachorro = {
    "tipo": "Cachorro",
    "nome": "Rex",
    "raca": "Labrador",
    "dono": pessoa   # Aqui criamos uma relação: o dono é o frame 'pessoa'
}

# Exibição dos frames com hierarquia
print("=== Frame: Cachorro ===")
for atributo, valor in cachorro.items():
    if isinstance(valor, dict):
        print(f"{atributo}: {valor['nome']} ({valor['tipo']})")  # mostra o nome do frame referenciado
    else:
        print(f"{atributo}: {valor}")

print("\n=== Frame: Pessoa ===")
for atributo, valor in pessoa.items():
    print(f"{atributo}: {valor}")
