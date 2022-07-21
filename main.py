from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from algorithm import ImageScraper


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
    return {"Root Request": 200}


@app.get("/grab/{link}")
def grab_images(link: Optional[str] = None):
    urlimages = ImageScraper('https://' + link)
    print(urlimages.url)
    urlimages.get_html()
    return urlimages.get_images()
