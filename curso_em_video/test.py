# salva como uaitech_scraper.py
import requests
from bs4 import BeautifulSoup
import re

url = "https://uaitech.eng.br"
res = requests.get(url, timeout=10)
soup = BeautifulSoup(res.text, "html.parser")

print("Título:", soup.title.string if soup.title else "Sem título")

emails = set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", soup.get_text()))
print("\nE-mails encontrados:", emails)

links = [a["href"] for a in soup.find_all("a", href=True)]
print("\nLinks encontrados:")
for link in links:
    print("-", link)

print("\nTextos visíveis:")
for tag in soup.find_all(["p", "h1", "h2", "h3", "li"]):
    texto = tag.get_text(strip=True)
    if texto:
        print("-", texto)
