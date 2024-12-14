import sys
import requests
from lxml import html


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []

    response = requests.get(url)
    if response.status_code != 200:
        print('chyba')
        return []
    
    root = html.fromstring(response.content)
    for h in ("a_href"):
        elements = root.xpath(f"//{h}")
        for el in elements:
            href = el.text_content()
            hrefs.append(href)
    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        all_hrefs = download_url_and_get_all_hrefs(url)
        for href in all_hrefs:
            print(href)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
