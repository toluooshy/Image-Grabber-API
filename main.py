from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from algorithm import ImageScraper


class Payload(BaseModel):
    link: str


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


@app.post("/grab")
def grab_images(data: Payload) -> dict:
    urlimages = ImageScraper('http://' + data.link)
    urlimages.get_html()
    return urlimages.get_images()
