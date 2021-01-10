import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/naomihasan/Desktop/WebScraper/chromedriver')
driver.get('https://www.glossier.com/products')
products = []
prices = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
driver.quit()

for a in soup.findAll(attrs="ProductCardContentWrapper-sc-1wi0jey-0 YgzWs"):
    name = a.find("p")
    if name not in products:
        products.append(name.text)


'''
for b in soup.findAll(attrs="sc-bdVaJa geJNWp"):
    name = b.find("div")
    if name not in prices:
        prices.append(name.text)
df = pd.DataFrame({'Products' : products, 'Prices': prices})
'''

df = pd.DataFrame({'Products' : products})
df.to_csv('GlossierProducts.csv', index='False', encoding= 'utf-8')


