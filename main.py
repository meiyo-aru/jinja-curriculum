from jinja2 import Environment, FileSystemLoader
from api import *
import requests
from googletrans import Translator

translator = Translator()
url_api = "https://curriculum-data-api.onrender.com"
env = Environment(loader=FileSystemLoader('templates'))

@app.get("/")
async def get_root():
    return {"mensagem": "curriculum_render_api no ar!"}

@app.head("/", status_code=status.HTTP_200_OK)
async def head_root():
    return None

@app.get("/get/about_me")
async def get_about_me(people_id: int = 1, language: str = "pt"):
    response = requests.get(url_api + "/get/people?people_id=" + people_id)
    about_me = env.get_template("about_me.html")
    
    if language == "pt":
        html = about_me.render(title_about_me="Sobre mim", 
                               about_me=response.about)
    else:
        html = about_me.render(title_about_me="About me", 
                               about_me=translator.translate(response.about, dest=language))
        
    return html

@app.get("/get/header")
async def get_about_me(people_id: int = 1, language: str = "pt"):
    response = requests.get(url_api + "/get/people?people_id=" + people_id)
    header = env.get_template("header.html")
    
    if language == "pt":
        html = header.render(linkedin=response.linkedin, 
                             mail=response.mail, 
                             phone=response.phone, 
                             address=response.address, 
                             positions=response.positions, 
                             name=response.name,
                             profile_title="Perfil")
    else:
        html = header.render(linkedin=response.linkedin, 
                             mail=response.mail, 
                             phone=response.phone, 
                             address=response.address, 
                             positions=response.positions, 
                             name=response.name,
                             profile_title=translator.translate("Perfil", dest=language))
        
    return html


