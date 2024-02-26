
def tabuada(valor):
    i = 1
    while i < 11:
        resultado = valor * i

        print(valor, "x", i, " = ", resultado)
        i = i + 1

def tabuada_um_vinte():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    intervalos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for numero in numeros:
        for intervalo in intervalos:
            resultado = numero * intervalo
            print(numero, " * ", intervalo, " = ", resultado)
        print("-----------------------------------------")

tabuada_um_vinte()