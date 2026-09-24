# Crie um sistema de login com dois dicionários: um que guarda as credenciais corretas, e outro dicionário que guarde as informações inseridas pelo usuário. Peça ao usuário para digitar o usuário e senha, e verifique se está correto de acordo com o primeiro dicionário.

# Se o usuário e a senha estão corretos → "Login bem-sucedido"

# Senão → "Usuário ou senha incorretos"

usuario = input("Digite seu usuario: ")
senha = input("Digite sua senha: ")

credenciais_corretas = {

    "usuario": "Ramon",
    "senha": "123"
}

credenciais_inseridas = {
    "usuario": usuario,
    "senha": senha
}

if credenciais_inseridas == credenciais_corretas:
    print("Login bem_sucedido!")
else:
    print("Usuário ou senha incorretos.")