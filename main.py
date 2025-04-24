from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "name": "Przemysław Włodarczyk",
        "linkedin_url": "https://www.linkedin.com/in/przemwlodarczyk/",
        "github_url": "https://github.com/wudjitzu",
        "img_url": "/static/img/img.jpg"
    })
