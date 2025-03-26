import requests
from bs4 import BeautifulSoup

# Simulam ca extragem date dintr-un URL real
url = "https://example.com/products"
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.txt, 'html.parser')

    # Gasim toate produsele
    products = soup.find_all('div', class_='product')

    for product in products:
        name = product.find('h2', class_='name').text.strip()
        price = product.find('span', class_='price').text.strip()
        print(f'Product: {name}, Price: {price}')
else:
    print(f'Failed to retrive data, status code: {response.status_code}')