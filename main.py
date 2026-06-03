from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "inicio.html", {"ano_actual": datetime.now().year})

@app.get("/inicio", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse(request, "inicio.html", {"ano_actual": datetime.now().year})

@app.get("/productos", response_class=HTMLResponse)
async def productos(request: Request):
    return templates.TemplateResponse(request, "productos.html", {"ano_actual": datetime.now().year})

@app.get("/pelocuidado", response_class=HTMLResponse)
async def pelocuidado(request: Request):
    return templates.TemplateResponse(request, "pelocuidado.html", {"ano_actual": datetime.now().year})

@app.get("/contacto", response_class=HTMLResponse)
async def contacto(request: Request):
    return templates.TemplateResponse(request, "contacto.html", {"ano_actual": datetime.now().year})
  
