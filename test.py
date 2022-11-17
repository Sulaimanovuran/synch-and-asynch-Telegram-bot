import requests
from bs4 import BeautifulSoup


def get_data():
    headers = {
        'Accept': '* / *',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }
    url = 'https://valuta.kg/'
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    currency = soup.find('div', class_='kurs-bar').find('div', class_='kurs-bar__rates').find_all('div',
                                                                                                  class_="kurs-bar__item")
    print('***********************\n')
    print(currency)
    print(len(currency))
    res = []
    for i in currency[1:]:
        for j in i.find_all('tr'):
            res.append(j.text.strip().replace(' ', ''))
    print('***********************\n')
    print(res)
    print('***********************\n')
    res2 = [i.split('\n') for i in res]
    print(res2)
    print('***********************\n')
    # res3 = [j for i in res2 for j in i if all([j != '', j != 'покупка', j != 'продажа'])]
    res3 = []
    for i in res2:
        for j in i:
            if j !='' and j !='покупка' and j != 'продажа':
                res3.append(j)


    return res3


print(get_data())
