# Função que aplica regras simples de diagnóstico de temperatura
def diagnosticar_temperatura(temp):
    if temp > 38:
        return "Pessoa está com febre."
    elif temp < 35:
        return "Pessoa está com hipotermia."
    else:
        return "Temperatura normal."

# Testando as regras
print(diagnosticar_temperatura(39))
print(diagnosticar_temperatura(36))
print(diagnosticar_temperatura(34))

'''
Comentário:

Cada if... elif... else é uma regra de decisão.

A função aplica o conhecimento médico codificado em forma lógica.
'''