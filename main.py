import time
from jinja2 import Environment, FileSystemLoader
from api import *
from fastapi.staticfiles import StaticFiles

from external_api import get_data_external_api

url_api = "https://curriculum-data-api.onrender.com" # url of data-api

env = Environment(loader = FileSystemLoader('templates')) # search templates in /templates
app.mount("/static", StaticFiles(directory="static"), name="static") # mount 'static' directory for give static archives (css, js)

@app.head("/", status_code = status.HTTP_200_OK) # endpoint for check api status
async def head_root():
    return None

# endpoint for give an complete html page
@app.get("/get", response_class=HTMLResponse)
async def serve_main_html(people_id: int = 1, language: str="pt"):
    try:
        url = url_api + "/get?people_id=" + str(people_id)
        response = await get_data_external_api(url)
                
        start = time.time()
        template = env.get_template("index.html") # load the index.html jinja2 template
        html = template.render(
            # about_me template
            about_me = response.get("about"),
            # header template
            linkedin = response.get("linkedin"), 
            mail = response.get("mail"), 
            phone_01 = response.get("phone_01"), 
            phone_02 = response.get("phone_02"), 
            address = response.get("address"), 
            positions = response.get("positions"), 
            name = response.get("name"),
            # academic_trainings template
            academic_trainings = response.get("academic_trainings"),
        )
        end = time.time()

        print("tempo renderização do template = " + str(end - start))
        return HTMLResponse(html)
    
    except Exception as e: # handle exception
        return HTMLResponse(f"Erro ao carregar a página principal: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @app.get("/get/about_me") # return an html with a section about the person from the resume
# async def get_about_me(people_id: int = 1, language: str = "pt"):
#     url_api_final = url_api + "/get/people?people_id=" +  str(people_id) # make final url for connect with external api
#     response = await get_data_external_api(url_api_final) # call function for handle exception and await
#     template = env.get_template("about_me.html") # load the template
    
#     # translate the html before send a response
#     html = template.render(
#         title_about_me = translator.translate("Sobre mim", dest = language).text, 
#         about_me = translator.translate(response.get("about"), dest = language).text
#     )
    
#     return Response(content=html, media_type="text/html")

# @app.get("/get/header", response_class = HTMLResponse) # return an html with template header
# async def get_header(people_id: int = 1, language: str = "pt"):
#     url_api_final = url_api + "/get/people?people_id=" +  str(people_id) # make final url for connect with external api
#     response = await get_data_external_api(url_api_final) # call function for handle exception and await
#     template = env.get_template("header.html") # load the template
    
#     # translate the html before send a response
#     html = template.render(
#         linkedin = response.get("linkedin"), 
#         mail = response.get("mail"), 
#         phone_title = translator.translate("Celular", dest = language).text,
#         phone_01 = response.get("phone_01"), 
#         phone_02 = response.get("phone_02"), 
#         address_title = translator.translate("Endereço", dest = language).text,
#         address = response.get("address"), 
#         positions = translator.translate(response.get("positions"), dest = language).text, 
#         name = response.get("name"),
#         profile_title = translator.translate("Perfil", dest = language).text
#     )
        
#     return html

# @app.get("/get/language", response_class = HTMLResponse) # return an html with template language
# async def get_language(language: str = "pt"):
#     template = env.get_template("language.html") # load the template
    
#     # translate the html before send a response
#     html = template.render(
#         language_title = translator.translate("Idioma", dest = language).text,
#         lang = language,
#         language_pt = translator.translate("Português", dest = language).text,
#         language_en = translator.translate("Inglês", dest = language).text
#     )
                
#     return html

# @app.get("/get/academic_training", response_class = HTMLResponse) # return an html with template academic_training
# async def get_academic_training(people_id: int = 1, language: str = "pt"):
#     url_api_final = url_api + "/get/academic_training?people_id=" +  str(people_id) # make final url for connect with external api
#     response = await get_data_external_api(url_api_final) # call function for handle exception and await
    
#     template = env.get_template("academic_training.html") # load the template
    
#     academic_trainings_translated = []
#     for item in response:
#         translated_item = {
#             "name" : translator.translate(item.get("name"), dest = language).text,
#             "level" : translator.translate(item.get("level"), dest = language).text,
#             "institution_title" : translator.translate("Instituição", dest = language).text,
#             "institution" : item.get("institution"),
#             "location_title" : translator.translate("Localização", dest = language).text,
#             "location" : item.get("address"),
#             "start_date_title" : translator.translate("Início", dest = language).text,
#             "start_date" : item.get("start_date"),
#             "end_date_title" : translator.translate("Fim", dest = language).text,
#             "end_date" : item.get("end_date")
#         }
#         academic_trainings_translated.append(translated_item)        
    
#     html = template.render(
#         academic_trainings = academic_trainings_translated,
#         academic_training_title = translator.translate("Formação Acadêmica", dest = language).text
#     )
    
#     return html




