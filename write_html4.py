import graphlib
from jinja2 import Environment, Template, FileSystemLoader
from fastapi import *
from backend.graph_functions import *
# , graph_type
def columnDisplayPage4(graphtotal):
    environment = Environment(loader=FileSystemLoader("templates/"))
    results_filename = "templates/page4-results.html"
    results_template = environment.get_template("/page-4.html")
    context = {
        "graphtotal": graphtotal
    }
 
    with open(results_filename, mode="w", encoding="utf-8") as results:
        results.write(results_template.render(context))
        print(f"... wrote {results_filename}")

