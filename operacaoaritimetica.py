

def calculo_area_retangulo(base, altura):
    area = base * altura
    return area

def calculo_area_quadrado(diagonal):
     area = diagonal * diagonal / 2
     return area

print(calculo_area_retangulo(5, 10))
print(f'A area do quadrado é: {calculo_area_quadrado(6)}')