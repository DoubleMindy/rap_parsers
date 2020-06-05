from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re
#import progressbar

RAPPER = input("ПИШИ СЮДА РЭПЕРА (МАЛЕНЬКИМИ БУКВАМИ НА АНГЛИЙСКОМ С ПРОБЕЛАМИ (типа dino mc 47):")
site = "http://rap-text.ru/" + RAPPER.replace(r' ', '_')
req = Request(site + ".html", headers = {'User-Agent':'Chrome/63.0.3239.132'})
page = urlopen(req).read()
soup = BeautifulSoup(page, 'html.parser')
print("Creating of doucment...")
i = 0
all_links = soup.findAll('a', attrs = {'href': re.compile("^" + site)})
#bar = progressbar.ProgressBar(maxval=len(all_links)).start()
for a in all_links:
    site = a.get('href')
    req = Request(site, headers = {'User-Agent':'Chrome/63.0.3239.132'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page, 'lxml')
    i += 1
    with open('ALL_SONGS.txt', 'a') as f:
        pre_text = soup.findAll('div', attrs = {'style' : 'font-size: 1.2em;'})
        p = [row.text for row in pre_text]
        for elems in p:
            f.write(str(elems))
    #bar.update(i)
#bar.finish()
print("===DONE!===")