import requests
from bs4 import BeautifulSoup
import pyperclip

def extraer_texto(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
    }
    contenido = requests.get(link, headers=headers)
    
    if contenido.status_code != 200:
        return f'Error {contenido.status_code}: {contenido.reason}'

    soup = BeautifulSoup(contenido.text, 'html.parser')
    texto = soup.get_text()
    return texto

def main():
    while True:
        link = input('Introduce el enlace de la página que deseas escrapear: ')
        texto = extraer_texto(link)
        print('\nTexto extraído:\n')
        print(texto)

        pyperclip.copy(texto)
        print('\nEl texto ha sido copiado al portapapeles.')

        opcion = input('¿Deseas escrapear otra página? [S/N]: ').lower()
        if opcion != 's':
            break

if __name__ == '__main__':
    main()