from jinja2 import Environment, FileSystemLoader
from api import *

env = Environment(loader=FileSystemLoader('templates'))
about_me = env.get_template('about_me.html')

html_about_me = about_me.render(about_me="opa", teste="teste", nome="pedrin")

@app.get("/")
def root():
    return {"mensagem": "curriculum_render_api no ar!"}

@app.get("/get/about_me")
def get_about_me():
    return 