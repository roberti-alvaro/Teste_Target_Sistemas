# Pegar do usuário o texto a ser invertido
texto = input("Digite uma palavra ou frase: ")

# loop pelos caracteres do texto de trás pra frente e adicionando um por um a nova variável texto_invertido
texto_invertido = ""

for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]

# Exibição do novo texto, agora invertido
print(texto_invertido)
