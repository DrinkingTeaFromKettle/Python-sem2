def policzPuste(tablica: list[list[int | None]]) -> int:
    puste = 0
    for i in tablica:
        puste += sum(1 for j in i if j is None)
    return puste