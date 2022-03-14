from typing import Optional

from threading import current_thread
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
import requests


class ImageScraper:
    def __init__(self, url):
        self.url = url
        self.html = ""
        self.images = []

    def get_html(self):
        """
        This function gets the raw html code from the website defined in self.url

        Takes: self
        Use: defines self.html
        Returns: self.html
        """
        try:
            self.html = BeautifulSoup(requests.get(self.url).content, 'lxml')
            return self.html
        except TypeError:
            print(
                "This function needs an object of the type 'string' to be passed into it to work.")

    def get_images(self):
        """
        This function gets the image src urls from the raw html defined in self.html

        Takes: self
        Use: defines self.images
        Returns: self.images
        """
        imgs = self.html.find_all('img')
        for img in imgs:
            try:
                if len(img['src']) > 0:
                    if img['src'][0:2] == '//':
                        self.images.append(img['src'][2:])
                    elif img['src'][0:1] == '/':
                        self.images.append(self.url+img['src'][1:])
                    else:
                        self.images.append(img['src'])
            except KeyError:
                pass
        return self.images


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "https://main.d5g9oyj5u2wzt.amplifyapp.com",
    "http://main.d5g9oyj5u2wzt.amplifyapp.com",
    "main.d5g9oyj5u2wzt.amplifyapp.com",
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
    urlimage = ImageScraper(website)
    urlimage.get_html()
    return urlimage.get_images()
