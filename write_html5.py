import graphlib
from jinja2 import Environment, Template, FileSystemLoader
from fastapi import *
from backend.graph_functions import *

def columnDisplayPage5(graphtotal):
    graph_num = graphtotal + 1
    environment = Environment(loader=FileSystemLoader("templates/"))
    results_filename = "templates/page5-results.html"
    results_template = environment.get_template("/page-5.html")

    imgpath = "static/1.png"
    #os.path.abspath(file)  # Figures out the absolute path for you in case your working directory moves around.
    context = {
        "graphtotal": graphtotal,
        "imgpath": imgpath


    }

    with open(results_filename, mode="w", encoding="utf-8") as results:
        results.write(results_template.render(context))
        print(f"... wrote {results_filename}")

# columnDisplayPage3(graphtotal, headers1, headers2, headers3, headers4, headers5)