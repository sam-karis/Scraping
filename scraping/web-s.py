from bs4 import BeautifulSoup
import requests
import csv

url = 'https://report.boonecountymo.org/mrcjava/servlet/RMS01_MP.I00030s'
response = requests.get(url, headers={'User-Agent': 'Chrome/78.0.3904.108'})
html = response.content

soup = BeautifulSoup(html, 'html.parser')
columns = [column.text.strip() for column in soup.select('.data-table .table-header th')]
table = soup.find('tbody', attrs={'class': 'stripe'})

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.strip().replace('&nbsp;', '')
        list_of_cells.append(text)
        list_of_rows.append(list_of_cells)

with open("./inmates.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    writer.writerows(list_of_rows)
