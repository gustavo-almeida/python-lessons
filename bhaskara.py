import math

def delta(a,b,c):
    return (b ** 2) - 4 * a * c

def main():
    a_digitado = float(input("Qual o valor de A da equação de segundo grau? "))
    b_digitado = float(input("Qual o valor de B da equação de segundo grau? "))
    c_digitado = float(input("Qual o valor de C da equação de segundo grau? "))
    imprime_raizes(a_digitado,b_digitado,c_digitado)

def imprime_raizes(a,b,c):
    d = delta(a,b,c)
    if d == 0:
        raiz = -b / (2 * a)
        print ("Essa equação possui raízes iguais: ", raiz)
    elif d > 0:
        raizDelta = math.sqrt(d)
        raiz1 = (-b + raizDelta) / (2 * a)
        raiz2 = (-b - raizDelta) / (2 * a)
        print ("Essa equação possui duas raízes diferentes: ", raiz1, "e", raiz2)
    else:
        print ("Essa equação não tem raízes reais.")
