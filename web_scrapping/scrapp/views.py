from django.shortcuts import render

# Create your views here.
from bs4 import BeautifulSoup
import requests


def index(request):
    url = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    titles = []
    prices = []
    images = []
    description = []
    links = []

    for data in soup.find_all('div', attrs={'class': '_2kHMtA'}):
        title = data.find('div', attrs={'class': '_4rR01T'})
        price = data.find('div', attrs={'class': '_30jeq3 _1_WHN1'})
        image = data.find('img', attrs={'class': '_396cs4 _3exPp9'})
        desc = data.find('ul', attrs={'class': '_1xgFaf'})
        lk = data.find('a', attrs={'class': '_1fQZEK'})

        lst = []
        for li in desc:
            # print(li.string)
            lst.append(li.string)
        description.append(lst)
        titles.append(title.string)
        prices.append(price.string)
        images.append(image.get('src'))
        links.append(lk.get('href'))
    data = zip(titles, prices, images, description, links)
    context = {
        'data': data
    }
    return render(request, 'index.html', context)
