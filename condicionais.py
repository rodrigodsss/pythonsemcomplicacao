

def terreno_grande_pequeno(base, altura):
    terreno = base * altura
    if terreno > 100:
        return  "Terreno grande"
    else:
        return "Terreno pequeno"


def calculo_velocidade(aceleracao, v_inicial, tempo):
    velocidade = (v_inicial + aceleracao * tempo) * 3.6
    print(velocidade)
    if velocidade <= 40:
        return  "Veiculo muito lento"
    elif velocidade > 40 and velocidade <=60:
        return "Velocidade permitida"
    elif velocidade > 60 and velocidade <=80:
        return "Velocidade de cruzeiro"
    elif velocidade > 80 and velocidade <= 120:
        return "Veiculo rápido"
    return "Veiculo muito rápido"