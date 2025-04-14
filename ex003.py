'''Módulo 2: Estruturas de seleção ou condição - Como usar if em Python.'''
#O que devo fazer quando acordar?

devo_levantar = False
esta_muito_quente = True
esta_muito_frio = True


if devo_levantar == True:
    print('Lenvantar e preprar aquele café maroto!')
elif esta_muito_frio == True:
    print('Ficar na cama!')
elif esta_muito_quente == True:
    print('Aumentar o ventilador!')
else:
    print('Dormir mais 5 minutinhos!')