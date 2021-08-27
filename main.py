import bs4
import requests

result = requests.get("https://www.moneycontrol.com/stocks/marketinfo/marketcap/bse/index.html")
soup = bs4.BeautifulSoup(result.text, "lxml")

x = soup.select(".bl_12")
y = soup.select(".brdrgtgry")

print('Top 10 stock to invest in india according to www.moneycontrol.com are: ')

for i in range(1, 11):
	for item in x[i]:
	  print(str(i) + ". " + item.text)
