#input para o programa utilizar o número do usuário para o cálculo
valor = int(input("Digite um número inteiro: "))

#loop para gerar e exibir a sequência fibonacci até o número que o usuário digitou
a = 0 
b = 1
fibonacci = []

while b <= valor:
    fibonacci.append(b)
    a, b = b, a + b

print("A sequência fibonacci calculada é:")
print(fibonacci)
      
#Checagem se o valor digitado pertence a sequência fibonacci gerada
if valor in fibonacci:
    print(f"O número {valor} pertence à sequência de Fibonacci.")
else:
    print(f"O número {valor} não pertence à sequência de Fibonacci.")
