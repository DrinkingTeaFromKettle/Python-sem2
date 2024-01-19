import re
# obliczająca liczbę wyrazów w napisie,
def iloscWyrazow(napis: str) -> int:
    return len(re.findall(r'\w+', napis))


# odwracająca kolejność wyrazów,
def odwrocKolejnosc(napis: str) -> str:
    s = napis.split()[::-1]
    nowyNapis = []
    for w in s:
        nowyNapis.append(w)
    return " ".join(nowyNapis)

# usuwająca znaki białe w napisie.
def usunBiale(napis: str) -> str:
    return "".join(napis.split())