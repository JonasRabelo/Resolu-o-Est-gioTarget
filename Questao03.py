import json

minimo = 100000000
maximo = 0
soma = 0
dias_uteis = 0
dias = [0, 0]
	

with open ("dados.json") as file:
	dados = json.load(file)

for day in dados:
	if day["valor"] != 0.0:
		if day["valor"] > maximo:
			maximo = day["valor"]
			dias[0] = day["dia"]
		if day["valor"] < minimo:
			minimo = day["valor"]
			dias[1] = day["dia"]
		dias_uteis += 1
		soma += day["valor"]


media = soma / dias_uteis
dias_fat = 0

for i in dados:
	if i["valor"] > media:
		dias_fat += 1


print(f'O menor valor de faturamento ocorreu no dia {dias[1]}, tendo como valor de faturamento R$ {minimo}')
print(f'O maior valor de faturamento ocorreu no dia {dias[0]}, tendo como valor de faturamento R$ {maximo}')
print(f'Em {dias_fat} dias, o faturamento diário foi maior que a média mensal')