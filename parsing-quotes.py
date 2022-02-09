import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/' # URL site`s to parse 
response = requests.get(url) #GET RESPONSE
soup = BeautifulSoup(response.text, 'lxml') #Respone on lxml
quotes = soup.find_all("span"); # Find All span tags
print(quotes);#Print in programm shell
