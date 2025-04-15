'''Módulo 3: Estruturas de repetição.'''

'''Tipos de repetição
1. lopp indefinido (while): Quando o bloco de instruções será executado até que uma condição se torne falsa (estrutura WHILE)
2. loop definido (for): Quando o bloco de instruções será executado um número fixo de vezes (estrutura FOR)

Variável contadora: Utilizada para controlar a contagem do número de execuções do bloco de instruções.
Variável acumuladora: Geralmente usada para acumular resultados(valores) parciais dentro de uma repetição (usualmente, inicia-se com 0).'''

'''For - Usamos o loop definido ou lopp for quando sabemos previamente o número de vezes que um bloco de instruções será executado.
A função range retorna uma lista de valores consecutivos comenado com o valor inicial, menores que o valor final, sendo incrementado em um determinado passo.

    for varialvel in range(inicio, fim, passo):
        
O valor inicial é opcional, se não for informado, o valor padrão será 0.
O valor final é obrigatório, se não for informado, o loop não será executado. O valor do passo é opcional, se não for informado, o valor padrão será 1.
O valor do passo pode ser negativo, nesse caso o valor inicial deve ser maior que o valor final. Se o valor do passo for 0, ocorrerá um erro de execução.

exemplo:
    for cont in range(0, 10, 1):
        print(cont)
        range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # 10 não é incluído na lista.
    
    for cont in range(6):
        print(cont)
        range = [0, 1, 2, 3, 4, 5]
        # 6 não é incluído na lista.
    
    for cont in range(0, 10, 2):
        print(cont)
        range = [0, 2, 4, 6, 8]
        # 10 não é incluído na lista.

        '''