'''Módulo 2: Estruturas de seleção ou condição

* Operadores relacionais e lógicos
* Seleção simples
* Seleção composta
* Seleção encadeada'''

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilos: "))
imc = peso / (altura ** 2)

print("Seu IMC é: " "{:.2f}".format(imc))

if imc < 18.5: 
    print("Seu IMC está abaixo do peso.")
elif imc >= 18.5 and imc <= 24.9:
    print("Seu IMC está na faixa ideal.")
elif imc >= 25.0 and imc <= 29.9:
    print("Seu IMC está com sobrepeso.")
else: 
    print("Seu IMC está com obesidade.")

