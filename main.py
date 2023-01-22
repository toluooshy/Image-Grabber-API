from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from algorithm import ImageScraper


class Payload(BaseModel):
    url: str


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "https://americans-flags-nft.herokuapp.com",
    "http://americans-flags-nft.herokuapp.com",
    "americans-flags-nft.herokuapp.com",
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


@app.post("/grab")
def grab_images(data: Payload) -> dict:
    urlimages = ImageScraper('http://' + data.url)
    urlimages.get_html()
    return urlimages.get_images()
