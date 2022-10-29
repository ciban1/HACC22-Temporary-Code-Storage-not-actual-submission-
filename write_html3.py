import graphlib
from jinja2 import Environment, Template, FileSystemLoader
from fastapi import *
from backend.graph_functions import *

# graphtotal = 3
# headers1 = ['County1', 'Date1']
# headers2 = ['Urban Land Percentage2', 'Date2']
# headers3 = ['Urban Land Percentage2', 'Date2']
# headers4 = ['Urban Land Percentage2', 'Date2']
# headers5 = []

graph_count = [1, 2, 3, 4, 5]

def columnDisplayPage3(graphtotal, headers1, headers2, headers3, headers4, headers5):
    graph_num = graphtotal + 1
    environment = Environment(loader=FileSystemLoader("templates/"))
    print(graphtotal)
    headers_list = ["he1", "he2", "he3", "he4", "he5"]
    results_filename = "templates/page3-results.html"
    results_template = environment.get_template("/page-3.html")
    context = {
        "graph_num": graph_num,
        "graphtotal": graphtotal,
        "headers1": headers1,
        "headers2": headers2,
        "headers3": headers3,
        "headers4": headers4,
        "headers5": headers5,
        
    }

    with open(results_filename, mode="w", encoding="utf-8") as results:
        results.write(results_template.render(context))
        print(f"... wrote {results_filename}")

# columnDisplayPage3(graphtotal, headers1, headers2, headers3, headers4, headers5)