#Criação de um dicionário com os valores informados
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Somar o valor total de faturamento mensal da distribuidora
fat_total = sum(faturamento.values())

print("A participação dos estados em relação ao total mensal da distribuidora foram:")

# Loop pelos estados calculando o percentual de representação de cada um
for estado, valor in faturamento.items():
    participacao = (valor / fat_total) * 100
    print(f"{estado} foi de {participacao:.2f}%.")