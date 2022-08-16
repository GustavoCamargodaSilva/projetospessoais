#Calculadora de IMC

print("******************************")
print("Bem vindo a calculadora de IMC")
print("******************************")

peso = float(input("Qual seu peso?"))
altura = float(input("Qual sua altura?"))

imc = peso / pow(altura , 2)
print("Seu Indice de massa corporal é:", round(imc,2))

magreza = imc < 18.5
normal = imc >= 18.5 and imc <= 24.9
sobrepeso = imc >= 25 and imc <= 29.9
obesidade = imc >= 30 and imc <= 39.9


if (magreza):
    print("Você está muito magro, precisa se alimentar mais!!")
elif (normal):
    print("Parabéns, você está no seu pesoa ideal!!")
elif (sobrepeso):
    print("Cuidado!!Você está com sobrepeso")
elif (obesidade):
    print("Você está obeso, deve procurar um nutricionista!!")
else:
    print("Você está com obesidade grave, deve procurar um nutricionista o mais rápido possível")


