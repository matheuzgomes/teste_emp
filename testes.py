import pytest
from main import Store

class Test:
    def test_motoboys_correto(self):
        motoboy = Store("moto 2")
        assert motoboy

    def test_campo_errado_inteiro(self):
        with pytest.raises(Exception) as error:
            Store(100)

        assert str(error.value) == "Motoboy name must be an string"

    def test_campo_errado_nome_invalido(self):
        with pytest.raises(Exception) as error:
            Store("corredor 1")

        assert str(error.value) == "Not a valid motoboy name"

    def test_campo_mao_registrado(self):
        with pytest.raises(Exception) as error:
            Store("moto 6")

        assert str(error.value) == "Motoboy not registered"

