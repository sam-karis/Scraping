from bs4 import BeautifulSoup
import requests
import csv

url = 'https://report.boonecountymo.org/mrcjava/servlet/RMS01_MP.I00030s'
response = requests.get(url, headers={'User-Agent': 'Chrome/78.0.3904.108'})
html = response.content
print(html)

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('tbody', attrs={'class': 'stripe'})

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
    print (list_of_rows)

outfile = open("./inmates.csv", "r+")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)