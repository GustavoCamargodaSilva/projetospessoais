#Validação usuário e senha com IF e Else

usuario = input("Qual seu usuário?")

if usuario != "Gustavo":
    print("Este usuário não existe.")
if usuario == "Gustavo":
    senha = input("Qual a sua senha?")
    if senha == "Gustavo@123":
        print("Bem vindo ao terminal Gustavo")
    else:
        print("Senha incorreta")
