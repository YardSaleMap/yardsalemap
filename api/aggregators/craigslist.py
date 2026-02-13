import requests
from bs4 import BeautifulSoup


def scrape_craigslist(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    listings = []

    for item in soup.find_all('li', class_='result-row'):
        title = item.find('a', class_='result-title hdrlnk').text
        link = item.find('a', class_='result-title hdrlnk')['href']
        price = item.find('span', class_='result-price')
        price = price.text if price else 'N/A'

        listings.append({'title': title, 'link': link, 'price': price})

    return listings
