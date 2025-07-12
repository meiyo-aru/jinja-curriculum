from jinja2 import Environment, FileSystemLoader
from api import *
import requests
from googletrans import Translator
from fastapi.staticfiles import StaticFiles

translator = Translator() # translator definition

url_api = "https://curriculum-data-api.onrender.com" # url of data-api

env = Environment(loader = FileSystemLoader('templates')) # search templates in /templates
app.mount("/static", StaticFiles(directory="static"), name="static") # mount 'static' directory for give static archives (css, js)

@app.get("/") # root endpoint
async def get_root():
    return {"mensagem": "curriculum_render_api no ar!"}

@app.head("/", status_code = status.HTTP_200_OK) # endpoint for check api status
async def head_root():
    return None

@app.get("/get/about_me") # return a html with a section about the person from the resume
async def get_about_me(people_id: int = 1, language: str = "pt"):
    response = requests.get(url_api + "/get/people?people_id=" + str(people_id)).json() # GET request for data-api, receive a json with person info and convert to dictionary
    template = env.get_template("about_me.html") # load the template
    
    # translate the html before send a response
    html = template.render(title_about_me = translator.translate("Sobre mim", dest = language).text, 
                            about_me = translator.translate(response.get("about"), dest = language).text)
    
    return Response(content=html, media_type="text/html")

@app.get("/get/header", response_class = HTMLResponse) # return an html with page header
async def get_header(people_id: int = 1, language: str = "pt"):
    response = requests.get(url_api + "/get/people?people_id=" +  str(people_id)).json() # GET request for data-api, receive a json with person info and convert to dictionary
    template = env.get_template("header.html") # load the template
    
    # translate the html before send a response
    html = template.render(linkedin = response.get("linkedin"), 
                            mail = response.get("mail"), 
                            phone_title = translator.translate("Celular", dest = language).text,
                            phone_01 = response.get("phone_01"), 
                            phone_02 = response.get("phone_02"), 
                            address_title = translator.translate("Endereço", dest = language).text,
                            address = response.get("address"), 
                            positions = translator.translate(response.get("positions"), dest = language).text, 
                            name = response.get("name"),
                            profile_title = translator.translate("Perfil", dest = language).text)
        
    return html

@app.get("/get/language", response_class = HTMLResponse) # return an html with page header
async def get_language(language: str = "pt"):
    template = env.get_template("language.html") # load the template
    
    # translate the html before send a response
    html = template.render(language_title = translator.translate("Idioma", dest = language).text,
                            lang = language,
                            language_pt = translator.translate("Português", dest = language).text,
                            language_en = translator.translate("Inglês", dest = language).text)
                
    return html



