# Web Scraper Script

This Python script allows you to scrape the text content from a webpage and copy it to your clipboard. It uses the `requests` library to fetch the webpage content, `BeautifulSoup` to parse and extract the text, and `pyperclip` to copy the extracted text to your clipboard.

## Features
- Scrapes the text from any given webpage.
- Copies the extracted text to the clipboard for easy use.
- Repeats the scraping process until the user decides to stop.

## Requirements
Before running the script, make sure you have the following Python libraries installed:
- `requests`
- `beautifulsoup4`
- `pyperclip`

You can install them using `pip`:
```bash
pip install requests beautifulsoup4 pyperclip
```

## How to Use

1. Run the script by executing `python scraper.py` in your terminal.
2. Enter the URL of the webpage you wish to scrape when prompted.
3. The script will display the text extracted from the page and copy it to your clipboard.
4. You can continue scraping other pages or exit by answering 'N' when asked if you want to scrape another page.

## Example

```bash
Introduce el enlace de la página que deseas escrapear: https://example.com
Texto extraído:
[The extracted text from the webpage will be displayed here]

El texto ha sido copiado al portapapeles.

¿Deseas escrapear otra página? [S/N]: N
```

## Notes
- The script uses a custom `User-Agent` header to mimic a request from a web browser.
- If the status code of the request is not 200 (OK), the script will return an error message with the status code and reason.
  
## License
This script is open-source and free to use under the MIT License.

 
