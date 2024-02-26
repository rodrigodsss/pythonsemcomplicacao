from unittest import TestCase
import condicionais

class Test(TestCase):
    def test_terreno_grande_pequeno (self):
        resultado = condicionais.terreno_grande_pequeno(11, 10)
        assert "Terreno grande" == resultado

    def test_terreno_pequeno(self):
        resultado = condicionais.terreno_grande_pequeno(9,10)
        assert "Terreno pequeno" == resultado

# Velocidade
    def test_veiculo_lento(self):
        resultado = condicionais.calculo_velocidade(10,1,1)
        assert "Veiculo muito lento" == resultado

    def test_velocidade_permitida(self):
        resultado = condicionais.calculo_velocidade(15,1,1)
        assert "Velocidade permitida" == resultado

    def test_velocidade_de_cruzeiro (self):
        resultado = condicionais.calculo_velocidade(5, 6, 3)
        assert "Velocidade de cruzeiro" == resultado

    def test_velocidade_rapido (self):
        resultado = condicionais.calculo_velocidade(15, 1, 10)
        assert "Veiculo muito rápido" == resultado