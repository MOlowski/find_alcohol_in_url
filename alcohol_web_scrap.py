from bs4 import BeautifulSoup
import requests
import json

base_url = 'https://www.thewhiskyexchange.com/brands/spirits'

# alcohol categories
categories = {
    'cognac': '/351/cognac',
    'armagnac': '/355/armagnac',
    'gin': '/338/gin',
    'jenever': '/623/jenever',
    'rum': '/339/rum',
    'vodka': '/335/vodka',
    'tequila': '/359/tequila',
    'liqueurs': '/343/liqueurs',
    'bitters': '/345/bitters-and-sprays',
    'vermouth/aperitif': '/365/vermouths-aperitifs-and-digestifs',
    'spirit': '/366/other-spirits'}

alcohols_list = []

for category, endpoint in categories.items():
    url = base_url+endpoint
    
    print(category, url)
    
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print("Soup")
        names = soup.find('div', class_="az-container")
    else:
        print(f"Error {response.status_code}")

    if names:
        alcohols = names.find_all('span', class_='az-item-name')

        for alcohol in alcohols:
            name = alcohol.get_text(strip=True)
            if category == 'vermouth/aperitif':
                category = ['vermouth', 'aperitif']
            alcohols_list.append({
                "name": alcohol,
                "category": category
            })
        print(f'found {len(alcohols)} alcohol brands')
    else:
        print('no alcohol brand found')


if len(alcohols_list) > 0:
    with open('alcohols.json', 'w') as file:
        file.dump(alcohols_list, file, indent=4)

# robots.txt says it's possible to get data from /brands endpoint
# but got 403 endpoint