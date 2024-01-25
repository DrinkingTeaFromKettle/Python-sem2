import re
def znajdz_date(napis):
    r = re.compile(r"(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[1,2])\.(20[0-2][0-3]|1[0-9]{3}|[1-9][0-9]{0,2}|[0-9])(p\.n\.e)?")
    match = r.search(napis)
    print(match.group() if match else "Nie znaleziono daty")

if __name__ == '__main__':
    znajdz_date("31.12.2023")
    znajdz_date("32.12.2023")
    znajdz_date("04.05.20p.n.e")
    znajdz_date("32.20")