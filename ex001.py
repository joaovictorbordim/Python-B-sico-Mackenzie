'''Módulo 1: Introdução ao Python
Elabore um código em Python que solicite os dados de ALTURA (em metros) e PESO 
(em quilos) de uma pessoa e calcule o IMC (Índice de Massa Corporal) dessa pessoa. O IMC é calculado pela fórmula:'''

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilos: "))
imc = peso / (altura ** 2)

print("Seu IMC é: " "{:.2f}".format(imc))

