# Frame representando um animal de estimação
frame_pet = {
    "Tipo": "Gato",
    "Nome": "Tom",
    "Cor": "Cinza",
    "Idade": 3,
    "Comportamentos": ["Miado", "Caçar", "Dormir"]
}

# Acessando atributos do frame
print(f"Tipo: {frame_pet['Tipo']}")
print(f"Nome: {frame_pet['Nome']}")
print(f"O {frame_pet['Tipo']} chamado {frame_pet['Nome']} gosta de {frame_pet['Comportamentos'][1]}.")

'''
Comentário:

Cada campo do dicionário representa um “slot” de conhecimento.

Os frames permitem organizar informações complexas sobre objetos ou situações.
'''