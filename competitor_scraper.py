import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_competitors(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    competitors = []
    for listing in soup.find_all('div', class_='listing'):
        name = listing.find('h2').text.strip()
        description = listing.find('p').text.strip()
        competitors.append({'Name': name, 'Description': description})
    
    return competitors

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    url = 'https://www.example.com/business-directory'
    competitors = scrape_competitors(url)
    save_to_csv(competitors, 'competitors.csv')
