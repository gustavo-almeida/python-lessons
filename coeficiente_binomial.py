def fatorial(valor):
    produto_total = valor
    while valor > 1:
        anterior = valor-1
        produto_total = produto_total * anterior
        valor = valor-1
    return produto_total

def testa_fatorial():
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")    

    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")
    
    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")
    
    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")

def numero_binomial(n, p):
    return fatorial(n) / (fatorial(n-p) * fatorial(p))
