import json

# Carregar arquivo fictício json para o python
with open("faturamento.json", "r") as file:
    faturamento = json.load(file)

#Loop pelos valores fornecidos pelo arquivo json e comparando qual foi o maior e qual foi o menor
menor_valor = float("inf")
maior_valor = float("-inf")
soma_valores = 0
dias_fat_acima_media = 0
dias_com_faturamento = 0

for valor in faturamento.values():
    if valor < menor_valor:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor

    #checa se o valor do arquivo json é zero, e caso não seja 0, soma os valores e adiciona contagem de dia com faturamento 
    if valor > 0:
        soma_valores += valor
        dias_com_faturamento += 1

# Calcula a média de faturamento excluindo os dias sem faturamento
media_faturamento = soma_valores / dias_com_faturamento

# Novo loop pelos valores do arquivo json novamente para contar os dias com faturamento acima da média
for valor in faturamento.values():
    if valor > media_faturamento:
        dias_fat_acima_media += 1

#
print(f"Menor valor de faturamento é: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento é: R$ {maior_valor:.2f}")
print(f"Dias com faturamento acima da média mensal de R${media_faturamento:.2f}: {dias_fat_acima_media}")
