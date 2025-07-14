import time
from typing import Dict, Any
from jinja2 import Environment, FileSystemLoader
from api import *
from fastapi.staticfiles import StaticFiles

from external_api import get_data_external_api

url_api = "https://curriculum-data-api.onrender.com" # url of data-api

env = Environment(
    loader = FileSystemLoader('templates'),
    autoescape=True
) # search templates in /templates
app.mount("/static", StaticFiles(directory="static"), name="static") # mount 'static' directory for give static archives (css, js)

@app.head("/", status_code = status.HTTP_200_OK) # endpoint for check api status
async def head_root():
    return None

# endpoint for give an complete html page
@app.get("/get", response_class=HTMLResponse)
async def serve_main_html(people_id: int = 1, language: str="pt"):
    try:
        url = url_api + "/get?people_id=" + str(people_id)
        
        start = time.time()
        response_from_api = get_data_external_api(url)
        end = time.time()
        print("Requisition time: " + str(end - start))
        
        # verify if response is an Response object or Dict, if Response then return
        if isinstance(response_from_api, Response):
            return response_from_api
        
        # if not a Response, assume are JSON (Dict)
        response: Dict[str, Any] = response_from_api 
        start = time.time()
        template = env.get_template("index.html") # load the index.html jinja2 template
        html = template.render(
            # about_me template
            about_me = response.get("about"),
            # header templatepip install -r requirements.txt
            linkedin = response.get("linkedin"), 
            mail = response.get("mail"), 
            phone_01 = response.get("phone_01"), 
            phone_02 = response.get("phone_02"), 
            address = response.get("address"), 
            positions = response.get("positions"), 
            name = response.get("name"),
            # academic_trainings template
            academic_trainings = response.get("academic_trainings"),
            experiences = response.get("experiences"),
            projects = response.get("projects_rel")
        )
        end = time.time()

        print("Template render time = " + str(end - start))
        return HTMLResponse(html)
    
    except Exception as e: # handle exception
        return HTMLResponse(f"Erro ao carregar a página principal: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
