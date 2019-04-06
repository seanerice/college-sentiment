from bs4 import BeautifulSoup
import urllib.request, urllib.error
import time, re, sys, random
from pathlib import Path

cache_dir = Path('unigo_pages')
cache_dir.mkdir(exist_ok=True)
base_url = 'https://www.unigo.com/'

def save_page(url, path):
    if not path.exists():
        print('downloading ' + url.split('/')[-1])
        while True:
            try:
                with urllib.request.urlopen(url) as response:
                    with path.open('wb') as f:
                        f.write(response.read())
                break
            except:
                print('network error, trying again...')
            finally:
                time.sleep(1.0 + random.random())
    with path.open('rb') as f:
        return BeautifulSoup(f.read(), features='html.parser')

def scrape_page(url, path, i):
    soup = save_page(url + '/' + str(i), path / (str(i) + '.html'))

    # for el in soup.find(id='reviewAnswerList').find_all('article'):
    #     starCount = el.find(class_='starCount')
    #     if starCount is None:
    #         print('no stars')
    #     else:
    #         starStyle = el.find(class_='starCount').attrs['style']
    #         print(int(re.findall('\d+', starStyle)[0])/20)
    #     comments = el.find_all('div', class_='show-on-open')
    #     print('\n'.join([c.p.string.strip() for c in comments]))


def get_rankings(url):
    # url = base_url + 'colleges/rensselaer-polytechnic-institute'
    path = cache_dir / url.split('/')[-1]
    path.mkdir(exist_ok=True)

    soup = save_page(url, path / '1.html')

    pageCountEl = soup.find(class_='PagedList-skipToLast')
    pagecount = int(pageCountEl.a.attrs['href'].split('/')[-1]) if pageCountEl is not None else 1

    for i in range(pagecount):
        scrape_page(url, path, i + 1) # pages are 1-indexed

def get_colleges():
    soup = save_page(base_url + 'colleges', cache_dir / 'colleges.html')
    states = [a.attrs['href'] for l in
                soup.find_all(class_='search_by_state_listing') for a in l.find_all('a')]
    for state in states:
        soup = save_page(base_url + state, cache_dir / (state.split('/')[-1] + '.html'))
        colleges = [a.attrs['href'] for a in soup.find_all(class_='bodyContent')[1].find_all('a')]
        for college in colleges:
            get_rankings(college)



get_colleges()
