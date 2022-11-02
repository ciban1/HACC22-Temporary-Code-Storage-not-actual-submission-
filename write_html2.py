# import graphlib
# from jinja2 import Environment, Template, FileSystemLoader
# from fastapi import *
# from backend.graph_functions import *


# def columnDisplayPage2(graph_num, columns):
#     graph_num = graph_num + 1
#     environment = Environment(loader=FileSystemLoader("templates/"))
#     print(graph_num)

#     results_filename = "templates/page2-results.html"
#     results_template = environment.get_template("/page-2.html")
#     context = {
#         "columns": columns,
#         "graph_num": graph_num
#     }
#     with open(results_filename, mode="w", encoding="utf-8") as results:
#         results.write(results_template.render(context))
#         print(f"... wrote {results_filename}")