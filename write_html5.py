import graphlib
from jinja2 import Environment, Template, FileSystemLoader
from fastapi import *
from backend.graph_functions import *
 
def columnDisplayPage5(graphtotal):
    environment = Environment(loader=FileSystemLoader("templates/"))
    results_filename = "templates/page5-results.html"
    results_template = environment.get_template("/page-5.html")
 
    #os.path.abspath(__file__)  # Figures out the absolute path for you in case your working directory moves around.
    context = {
        "graphtotal": graphtotal,
    }
 
    with open(results_filename, mode="w", encoding="utf-8") as results:
        results.write(results_template.render(context))
        print(f"... wrote {results_filename}")