from numpy import mean, median


def srednia(lista: list[int | float]) -> tuple[float, float]:
    sr = mean(lista)
    med = median(lista)
    return sr, med
