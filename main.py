from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get("/")
def index(request: Request):
    data = {
        "request": request, 
        "message": "Testing"
    }
    return templates.TemplateResponse("index.html", data)