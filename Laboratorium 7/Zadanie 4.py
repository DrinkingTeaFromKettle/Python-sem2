import pytest
from Prostokat import Prostokat

def test_init():
    p = Prostokat(4, 6)
    assert p.a == 4, "Długość boku a prostokąta powinna wynosić 4"
    assert p.b == 6, "Długość boku b prostokąta powinna wynosić 6"
def test_obwód():
    p = Prostokat(4,4)
    assert p.obwod() == 16, "Obwód powinien wynosić 16"
def test_pole():
    p = Prostokat(4,10)
    assert p.pole() == 40, "Pole powininno wynosić 40"

