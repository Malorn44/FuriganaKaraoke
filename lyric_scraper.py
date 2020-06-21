# PROBABLY NOT NEEDED
from urllib.parse import quote, unquote


import requests as rep
from bs4 import BeautifulSoup


def search(keyword):
    searchtext = 'http://www.uta-net.com/search/?Aselect=2&Bselect=3&Keyword='+keyword
    page = rep.get(searchtext)
    return (page, searchtext)



text = ''
while(text!='stop'):
    text = input()
    if (text=='stop'):
        break

    page, searchtext = search(text)

    soup = BeautifulSoup(page.text, 'html.parser')

    song_names = soup.find_all('td', class_ = 'td1')
    singer_names = soup.find_all('td', class_ = 'td2')
    lyricists_names = soup.find_all('td', class_ = 'td3')
    composer_names = soup.find_all('td', class_ = 'td4')
    starting_lyrics = soup.find_all('td', class_ = 'td5')
    
    for i in range(len(song_names)):
        print(song_names[i].a['href'], singer_names[i].text, lyricists_names[i].text, composer_names[i].text, starting_lyrics[i].text)