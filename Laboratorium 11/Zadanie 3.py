from datetime import datetime, timedelta

import requests
import xml.dom.minidom as xml

if __name__ == "__main__":
    start_date = datetime.now() - timedelta(days=30)
    url = f"http://api.nbp.pl/api/cenyzlota/{start_date.strftime('%Y-%m-%d')}/{datetime.now().strftime('%Y-%m-%d')}"
    format="XML"
    xml_data=requests.get(url+f"?format={format}").text
    data = xml.parseString(xml_data)
    ceny = data.getElementsByTagName("CenaZlota")
    suma = 0.
    for cena in ceny:
        print(f"W dniu {cena.getElementsByTagName('Data')[0].firstChild.nodeValue} cena złota "
              f"wynisła {cena.getElementsByTagName('Cena')[0].firstChild.nodeValue} ")
        suma += float(cena.getElementsByTagName('Cena')[0].firstChild.nodeValue)
    print(f"Średnia cena złota : {suma/len(ceny):.2f}")
