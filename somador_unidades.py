valor = int(input("Digite o valor a ter as unidades somadas: "))
soma = 0

while valor != valor % 10:
    soma = soma + valor % 10
    valor = valor // 10
soma = soma + valor % 10
print("Soma das unidades: ", soma)
