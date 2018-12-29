from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Some<b>bad<i>HTML")

print(soup.prettify())

#print(soup)
print(soup.find(text="bad"))

print(soup.i)

