'''SEM BOAS PRATICAS-------------------------------------------'''

def maior(a,b):
    return a if a > b else b
a = int(input('digite o primeiro numero'))
b = int(input('digite o segundo numero'))
print(maior(a, b))

'''COM BOAS PRATICAS-------------------------------------------'''

def verificar_numero_maior(numero1,numero2):
    return numero1 if numero1 > numero2 else numero2
try:
    numero1 = int(input('digite o primeiro numero'))
    numero2 = int(input('digite o segundo numero'))
    print(verificar_numero_maior(numero1, numero2))
except ValueError:
    print('digite um valor valido')