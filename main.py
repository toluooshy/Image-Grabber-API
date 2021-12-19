from typing import Optional

from threading import current_thread
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from bs4 import BeautifulSoup
import requests
import html


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


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "http://cup-noodle-app.herokuapp.com",
    "https://cup-noodle-app.herokuapp.com",
    "cup-noodle-app.herokuapp.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/url/{link}")
def read_item(link: Optional[str] = None):
    return geturl("http://" + link)
