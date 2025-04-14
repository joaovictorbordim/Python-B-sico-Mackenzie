'''Módulo 2: Estruturas de seleção ou condição - Como usar def em Python.'''

'''Função -> É um bloco de código reutilizável
    outra vantagem é a organização'''


'''Como funicona:
    def name_da_funcao(parametros):
        instrução 1
        instrução 2
        ...
        return valor (opcional)'''

def calcular_imposto(valor):
    if valor < 1000: 
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.13
    else:
        imposto = valor * 0.20
    return imposto

preco_produto1 = 2500
preco_produto2 = 3500
imposto_produto1 = calcular_imposto(preco_produto1)
imposto_produto2 = calcular_imposto(preco_produto2)

print(imposto_produto1)
print(imposto_produto2)

