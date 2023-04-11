sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = outros + sp + rj + mg + es
print('=======================================')
print("Valor total faturado: ", total)
print("São Paulo representa ", sp / total * 100, "%  do valor total")
print("Rio de Janeiro representa ", rj / total * 100, "%  do valor total")
print("Minas Gerais representa ", mg / total * 100, "%  do valor total")
print("Espírito Santo representa ", es / total * 100, "%  do valor total")
print("Outros estados representam ", outros / total * 100, "%  do valor total")