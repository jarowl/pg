import sys
import requests
from bs4 import BeautifulSoup


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    try:
        hrefs = []
        response = requests.get(url)

            # Zkontrolujeme, zda je odpověď úspěšná (status code 200)
        if response.status_code == 200:

            # Vytvoříme objekt BeautifulSoup pro analýzu HTML
            soup = BeautifulSoup(response.content, 'html.parser')

            # Najdeme všechny <a> tagy s atributem href
            for link in soup.find_all('a'):
                hrefs.append(link.get('href'))
        else:
            print(f"Chyba při stahování stránky: {response.status_code}")

    except Exception as e:
        print(f"Došlo k chybě při načítání URL: {e}")
    
    # Vrátíme seznam nalezených odkazů
    return hrefs

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
        for href in hrefs:
            print(href)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
