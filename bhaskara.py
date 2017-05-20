import math

a = float(input("Qual o valor de A da equação de segundo grau? "))
b = float(input("Qual o valor de B da equação de segundo grau? "))
c = float(input("Qual o valor de C da equação de segundo grau? "))

delta = (b ** 2) - 4 * a * c

if delta == 0:
    raiz = -b / (2 * a)
    print ("Essa equação possui raízes iguais: ", raiz)
elif delta > 0:
    raizDelta = math.sqrt(delta)
    raiz1 = (-b + raizDelta) / (2 * a)
    raiz2 = (-b - raizDelta) / (2 * a)
    print ("Essa equação possui duas raízes diferentes: ", raiz1, "e", raiz2)
else:
    print ("Essa equação não tem raízes reais.")
