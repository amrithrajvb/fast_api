from typing import Union

from fastapi import FastAPI,Request
from starlette.templating import Jinja2Templates

app = FastAPI()

template=Jinja2Templates(directory="templates")

@app.get("/")
def home(request:Request):
    return template.TemplateResponse("index.html",{"request":request})

@app.get("/signup")
def SignUp(request:Request):
    return template.TemplateResponse("Signup.html",{"request":request})
