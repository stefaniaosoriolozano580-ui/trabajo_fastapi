from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def inicio(request: Request):
    return templates.TemplateResponse("inicio.html", {"request": request})

@app.get("/productos")
def productos(request: Request):
    return templates.TemplateResponse("productos.html", {"request": request})

@app.get("/cuidado-pelo")
def cuidado(request: Request):
    return templates.TemplateResponse("cuidadopelo.html", {"request": request})

@app.get("/contacto")
def contacto(request: Request):
    return templates.TemplateResponse("contacto.html", {"request": request})
