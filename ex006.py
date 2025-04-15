'''Módulo 3: Estruturas de repetição.'''

'''Tipos de repetição
1. lopp indefinido (while): Quando o bloco de instruções será executado até que uma condição se torne falsa (estrutura WHILE)
2. loop definido (for): Quando o bloco de instruções será executado um número fixo de vezes (estrutura FOR)

Variável contadora: Utilizada para controlar a contagem do número de execuções do bloco de instruções.
Variável acumuladora: Geralmente usada para acumular resultados(valores) parciais dentro de uma repetição (usualmente, inicia-se com 0).'''

while True:
    n = int(input('Digite um número POSITIVO: '))
    if n> 0:
        break
print('Você digitou o número POSITIVO: ',n)