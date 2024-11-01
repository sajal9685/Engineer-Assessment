import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    table = soup.find('table')
    headers = [header.text for header in table.find_all('th')]
    rows = []
    
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if columns:
            rows.append([column.text.strip() for column in columns])
    
    return headers, rows

url = 'https://example.com/table'

headers, rows = scrape_website(url)

df = pd.DataFrame(rows, columns=headers)

excel_file = 'scraped_data.xlsx'
df.to_excel(excel_file, index=False)

print(f"Data successfully written to {excel_file}")
