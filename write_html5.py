import graphlib
from jinja2 import Environment, Template, FileSystemLoader
from fastapi import *
from backend.graph_functions import *

import base64
 
def columnDisplayPage5(graphtotal):
    environment = Environment(loader=FileSystemLoader("templates/"))
    results_filename = "templates/page5-results.html"
    results_template = environment.get_template("/page-5.html")
    
    if 1 <= graphtotal:
        with open("1.svg", "rb") as image_file:
            g1_base64 = str(base64.b64encode(image_file.read()),'utf-8')
    else:
        g1_base64 = None

    if 2 <= graphtotal:
        with open("2.svg", "rb") as image_file:
            g2_base64 = str(base64.b64encode(image_file.read()),'utf-8')
    else:
        g2_base64 = None

    if 3 <= graphtotal:
        with open("3.svg", "rb") as image_file:
            g3_base64 = str(base64.b64encode(image_file.read()),'utf-8')
    else:
        g3_base64 = None

    if 4 <= graphtotal:
        with open("4.svg", "rb") as image_file:
            g4_base64 = str(base64.b64encode(image_file.read()),'utf-8')
    else:
        g4_base64 = None

    if 5 <= graphtotal:
        with open("5.svg", "rb") as image_file:
            g5_base64 = str(base64.b64encode(image_file.read()),'utf-8')
    else:
        g5_base64 = None


    #os.path.abspath(__file__)  # Figures out the absolute path for you in case your working directory moves around.
    context = {
        "graphtotal": graphtotal,
        "g1_base64": g1_base64,
        "g2_base64": g2_base64,
        "g3_base64": g3_base64,
        "g4_base64": g4_base64,
        "g5_base64": g5_base64
    }
 
    with open(results_filename, mode="w", encoding="utf-8") as results:
        results.write(results_template.render(context))
        print(f"... wrote {results_filename}")