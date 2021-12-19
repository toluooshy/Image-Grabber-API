import html
import requests
from bs4 import BeautifulSoup


def geturl(link):
    html_page = requests.get(link)
    soup = BeautifulSoup(html_page.content, 'html.parser')
    images = soup.findAll('img', src=True, width=True)
    tempurl = None
    for image in images:
        if int(image['width']) > 50:
            tempurl = image['src']
            break

    if tempurl == None:
        r = requests.get(link)
        res = html.unescape(r.text)
        stringres = str(res)

        for i in range(stringres.count("</header>")):
            stringres = stringres.split("</header>", 1)[1]

        tempurl = stringres.split("<img", 1)[1].split(">", 1)[0].split(
            "src", 1)[1].split("=", 1)[1].split('"', 1)[1].split('"')[0]

    if tempurl[0] != "h":
        tempurl = link + "/" + tempurl
    return tempurl


print(geturl('https://www.google.com/'))
