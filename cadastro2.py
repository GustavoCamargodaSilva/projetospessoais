
pergunta = input("Gostaria de fazer o cadastro?")

if (pergunta != "sim"):
    print("Até mais..")
    exit()
else:
    email = input("Qual seu email?")
    senha = input("Qual a sua senha?")
print("Faça seu loguin")

login = input("Digite o seu email:")
password = input("Qual a sua senha?")

if login == email and password == senha:
    print("Logado com sucesso")
else:
    print("email ou senha estão incorretos")