from numpy import mean, median


def srednia(lista: list[int | float]) -> tuple[float, float]:
    sr = mean(lista)
    med = median(lista)
    return sr, med


def sortuj(krotka: tuple[int, ...]) -> list[int]:
    return sorted(krotka)


def policzPuste(tablica: list[list[int | None]]) -> int:
    puste = 0
    for i in tablica:
        puste += sum(1 for j in i if j is None)
    return puste
