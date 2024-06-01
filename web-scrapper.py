from bs4 import BeautifulSoup
import requests
url=input("enter the url:" )
page = requests.get(url)

Soup=BeautifulSoup(page.text, 'html')
#title:
print("Title of the page:")
Page_Title=Soup.find('title').text
print(Page_Title)
print("\n")
#first paragraph:
print("First paragraph:")
First_Paragraph=Soup.find('p').text
print(First_Paragraph)
print("\n")
#external links:
print("External links:")
External_links=[]
links=Soup.find_all('a')
for link in links:
  href=link.get('href')
  if href:
    External_links.append(href)
print(External_links)
print("\n")
#images:
images=Soup.find_all('img')
image_urls={}
print("images:")
print("printed in dictionary of the form - {alt-text:image-url}")
for image in images:
    url=image.get('src')
    alt=image.get('alt')
    image_urls[alt]=url
print(image_urls)