import graphlib
from jinja2 import Environment, Template, FileSystemLoader
from fastapi import *
from backend.graph_functions import *

def columnDisplayPage3(graphtotal, graph_type, headers1, headers2, headers3, headers4, headers5):
    graph_num = graphtotal + 1
    environment = Environment(loader=FileSystemLoader("templates/"))
    print(graphtotal)
    headers_list = ["he1", "he2", "he3", "he4", "he5"]
    results_filename = "templates/page3-results.html"
    results_template = environment.get_template("/page-3.html")
    context = {
        "graph_num": graph_num,
        "graph_type": graph_type,
        "headers1": headers1,
        "headers2": headers2,
        "headers3": headers3,
        "headers4": headers4,
        "headers5": headers5,
        "graphtotal": graphtotal
        
    }

    with open(results_filename, mode="w", encoding="utf-8") as results:
        results.write(results_template.render(context))
        print(f"... wrote {results_filename}")