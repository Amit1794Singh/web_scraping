import requests
from bs4 import BeautifulSoup
url = "https://prefeitura.pbh.gov.br/saude/licitacao/pregao-eletronico-151-2020"
r = requests.get(url)
print(r.status_code)
soup = BeautifulSoup(r.text,'html.parser')
#league_table = soup.find('table',class_="field-content")
league_table = soup.find('table',class_="views-field views-field-field-historico-da-licitacao")
#field field--name-field-title field--type-string field--label-hidden field__item
#print(league_table)
for item in league_table.find_all("tbody"):
    rows = item.find_all('tr')
    for row in rows:
        datess = row.find('td',class_="field field--name-field-data field--type-datetime field--label-hidden field__item")[1].text.strip()
        print(datess)
