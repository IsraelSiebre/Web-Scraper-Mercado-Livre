import requests
from bs4 import BeautifulSoup
import pandas as pd

#listas
nomes = []
valores = []
links = []

#produto
input_produto = input('Qual o produto? ')
url_base= 'https://lista.mercadolivre.com.br/'
request = requests.get(url_base + input_produto)
soup = BeautifulSoup(request.text, 'html.parser')
grupo_produtos = soup.find_all('li', attrs={'class': 'ui-search-layout__item shops__layout-item'})
print('Pesquisando produtos...')

for produto in grupo_produtos:  
    try:
        nomes.append(produto.find('h2', attrs={'class': 'ui-search-item__title shops__item-title'}).text) 
        valores.append(produto.find('span', attrs={'class': 'price-tag-amount'}).text)
        links.append(produto.find('a', attrs={'class': 'ui-search-item__group__element shops__items-group-details ui-search-link'})['href'])
    except:pass

#dataframe
df = pd.DataFrame(columns = ['NOME DO PRODUTO','PREÇO','LINK'])

df["NOME DO PRODUTO"] = nomes
df['PREÇO'] = valores
df['LINK'] = links


df.to_excel(f'{input_produto}.xlsx', index=False)
print("Relatorio Salvo!")
