from urllib.request import HTTPPasswordMgrWithDefaultRealm
import uvicorn
import re
from fastapi import FastAPI, Request, Form, Depends, UploadFile, File, Response
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sql_data import *
from write_html2test import *
from write_html3 import *
from write_html4 import *
from write_html5 import *
from backend.graph_functions import *
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route
from typing import List, Union, Optional
import ast
import starlette.status as status
 
# from send_graph_to_dir import * # now in backend folder
global csv_link
# from schemas import AwesomeForm  # uses schema file to bring in format of printing form data
 
app = FastAPI()
 
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
 
### how to page
@app.get("/how_to")
async def get_how_to(request: Request):
   return templates.TemplateResponse("how-to.html", {"request": request})
 
 
# page 1
@app.get('/', response_class=HTMLResponse)
async def get_first_form(request: Request):
   return templates.TemplateResponse("page-1.html", {"request": request})  # returns form
 
# html needs to allow scroll
@app.post('/', response_class=HTMLResponse)
async def post_first_form(request: Request, graphtotal: int = Form(...), csv_link: str = Form(...)):
   print('CSV link:', csv_link)
   print(graphtotal, 'graphs')
   # column_list = (column_headers(csv_link))
   column_list = str(column_headers(csv_link)).replace("&", "and")
   print(column_list)
   return fastapi.responses.RedirectResponse(f'/page_2/?graphtotal={graphtotal}&headers={column_list}&url={csv_link}', status_code=status.HTTP_302_FOUND)
 
##### page 2
@app.get('/page_2', response_class=HTMLResponse)
async def get_second_form(request: Request, graphtotal: Union[int, None] = None, headers: Union[str, None] = None, url: Union[str, None] = None):
   print("from get 2", graphtotal, headers)
   right_list = ast.literal_eval(headers)
   print(right_list)
   columnDisplayPage2(graphtotal, right_list)
   return templates.TemplateResponse("newpage2-results.html", {"request": request})
 
@app.post('/page_2', response_class=HTMLResponse)
def post_second_form(request: Request, g1xcheck: str = Form(...), g1ycheck: str = Form(...), g2xcheck: str = Form(None), g2ycheck: str = Form(None), g3xcheck: str = Form(None), g3ycheck: str = Form(None),
g4xcheck: str = Form(None), g4ycheck: str = Form(None), g5xcheck: str = Form(None), g5ycheck: str = Form(None),
column: list = Form(...), graph_type: list = Form(...), graphtotal: Union[int, None] = None, url: Union[str, None] = None):  # array of selected columns; use position
   print(column)
   print(graph_type)
   print("x", g1xcheck)
   print("y", g1ycheck)
   headers1 = []
   if 1 <= graphtotal:
      headers1.append(g1xcheck.replace("g1x", ""))
      headers1.append(g1ycheck.replace("g1y", ""))
  
   headers2 = [] 
   if 2 <= graphtotal:
      headers2.append(g2xcheck.replace("g2x", ""))
      headers2.append(g2ycheck.replace("g2y", ""))

   headers3 = []
   if 3 <= graphtotal:
      headers3.append(g3xcheck.replace("g3x", ""))
      headers3.append(g3ycheck.replace("g3y", ""))

   headers4 = []
   if 4 <= graphtotal:
      headers4.append(g4xcheck.replace("g4x", ""))
      headers4.append(g4ycheck.replace("g4y", ""))

   headers5 = []
   if 5 <= graphtotal:
      headers5.append(g5xcheck.replace("g5x", ""))
      headers5.append(g5ycheck.replace("g5y", ""))
   count = 1
   # while count < (int(graphtotal) + 1):
   #    for i in column:
   #       for char in i:
   #          if char == "1x":
   #             print("Fix this!")
   #             i = i.replace("g1x", "")
   #             if i not in headers1:
   #                headers1.append(i)
   #          if char == "1y":
   #             i = i.replace("g1y", "")
   #             if i not in headers1:
   #                headers1.append(i)
   #          elif char == "2":
   #             i = i.replace("2", "")
   #             if i not in headers2:
   #                headers2.append(i)
   #          elif char == "3":
   #             i = i.replace("3", "")
   #             if i not in headers3:
   #                headers3.append(i)
   #          elif char == "4":
   #             i = i.replace("4", "")
   #             if i not in headers4:
   #                headers4.append(i)
   #          elif char == "5":
   #             i = i.replace("5", "")
   #             if i not in headers5:
   #                headers5.append(i)
   #    count = count + 1
   print("h1", headers1)
   print(headers2)
   print(headers3)
   print(headers4)
   print(headers5)
   return fastapi.responses.RedirectResponse(f'/page_3/?graphtotal={graphtotal}&graph_type={graph_type}&h1={headers1}&h2={headers2}&h3={headers3}&h4={headers4}&h5={headers5}&url={url}', status_code=status.HTTP_302_FOUND)
 
### page 3
@app.get('/page_3', response_class=HTMLResponse)
async def get_third_form(request: Request, graphtotal: Union[int, None] = None, graph_type: Union[str, None] = None, h1: Union[str, None] = None, h2: Union[str, None] = None, h3: Union[str, None] = None, h4: Union[str, None] = None, h5: Union[str, None] = None, url: Union[str, None] = None):
   graph_type = ast.literal_eval(graph_type)
   print(type(h1))
   h1 = ast.literal_eval(h1)
   h2 = ast.literal_eval(h2)
   h3 = ast.literal_eval(h3)
   h4 = ast.literal_eval(h4)
   h5 = ast.literal_eval(h5)
   columnDisplayPage3(graphtotal, graph_type, h1, h2, h3, h4, h5)
   return templates.TemplateResponse("page3-results.html", {"request": request})
   
@app.post('/page_3', response_class=HTMLResponse)
async def post_third_form(request: Request, graphtotal: Union[int, None] = None, graph_type: Union[str, None] = None, hed1x: Optional[str] = Form(None), hed1y: Optional[str] = Form(None), hed2x: Optional[str] = Form(None), hed2y: Optional[str] = Form(None), hed3x: Optional[str] = Form(None), hed3y: Optional[str] = Form(None), hed4x: Optional[str] = Form(None), hed4y: Optional[str] = Form(None), hed5x: Optional[str] = Form(None), hed5y: Optional[str] = Form(None), url: Union[str, None] = None):
   graph_type = ast.literal_eval(graph_type)
   if 1 <= graphtotal:
      graph_one = {"g_type": graph_type[0], "x_axis_name": hed1x.replace("-x", ""), "y_axis_name": hed1y.replace("-y", ""), "color": '000000'}
      # settings=dict at the end
   else:
      graph_one = {}
   if 2 <= graphtotal:
      graph_two = {"g_type": graph_type[1], "x_axis_name": hed2x.replace("-x", ""), "y_axis_name": hed2y.replace("-y", ""), "color": "000000"}
      # "settings": dict at end
   else:
      graph_two = {}
   if 3 <= graphtotal:
      graph_three = {"g_type": graph_type[2], "x_axis_name": hed3x.replace("-x", ""), "y_axis_name": hed3y.replace("-y", ""), "color": "000000"}
   else:
      graph_three = {}
   if 4 <= graphtotal:
      graph_four = {"g_type": graph_type[3], "x_axis_name": hed4x.replace("-x", ""), "y_axis_name": hed4y.replace("-y", ""), "color": "000000"}
   else:
      graph_four = {}
   if 5 <= graphtotal:
      graph_five = {"g_type": graph_type[4], "x_axis_name": hed5x.replace("-x", ""), "y_axis_name": hed5y.replace("-y", ""), "color": "000000"}
   else:
      graph_five = {}
   print("555", graph_one)
   graph_configurations = [graph_one, graph_two, graph_three, graph_four, graph_five]
   return fastapi.responses.RedirectResponse(f'/page_4/?graphtotal={graphtotal}&graph_type={graph_type}&graph_configurations={graph_configurations}&url={url}', status_code=status.HTTP_302_FOUND)
 
   # return fastapi.responses.RedirectResponse(f'/page_4/?graphtotal={graphtotal}&graph_type={graph_type}&graph_one={graph_one}&graph_two={graph_two}&graph_three={graph_three}&graph_four={graph_four}&graph_five={graph_five}', status_code=status.HTTP_302_FOUND)
 
###page 4
@app.get('/page_4', response_class=HTMLResponse)
async def get_fourth_form(request: Request, graphtotal: Union[int, None] = None, graph_type: Union[str, None] = None, graph_configurations: Union[str, None] = None, url: Union[str, None] = None):
   print("THIS IS THE URL", url)
   graph_configurations = ast.literal_eval(graph_configurations)
 
   # columnDisplayPage4(graphtotal)
   # columnDisplayPage5(graphtotal)
   
   print(graph_configurations, type(graph_configurations))
   graph_one = graph_configurations[0]
   graph_two = graph_configurations[1]
   graph_three = graph_configurations[2]
   graph_four = graph_configurations[3]
   graph_five = graph_configurations[4]
   print(type(graph_one), graph_one)
   print(type(graph_two))
   print(type(graph_three))
   print(type(graph_four))
   print(type(graph_five))
   
   create_multiple_graphs(url, graph_configurations)
   columnDisplayPage4(graphtotal)
 
   return templates.TemplateResponse("page4-results.html", {"request": request})  # returns form
   
@app.post('/page_4', response_class=HTMLResponse)
def post_fourth_form(request: Request, graph1_name: str = Form(None), graph1_color: str = Form(None), graph2_name: Optional[str] = Form(None), graph2_color: Optional[str] = Form(None), graph3_name: Optional[str] = Form(None), graph3_color: Optional[str] = Form(None), graph4_name: Optional[str] = Form(None), graph4_color: Optional[str] = Form(None), graph5_name: Optional[str] = Form(None), graph5_color: Optional[str] = Form(None), graphtotal: Union[int, None] = None, graph_type: Union[str, None] = None, graph_configurations: Union[str, None] = None, url: Union[str, None] = None):
   # update color name
   graph_configurations = ast.literal_eval(graph_configurations)
   print("SUBMITTED 4")
   graph_one = graph_configurations[0]
   if "color" in graph_one:
      graph_one["color"] = graph1_color.replace("#", "")
   
   graph_two = graph_configurations[1]
   if "color" in graph_two:
      graph_two["color"] = graph2_color.replace("#", "")
   
   graph_three = graph_configurations[2]
   if "color" in graph_three:
      graph_three["color"] = graph3_color.replace("#", "")
 
   graph_four = graph_configurations[3]
   if "color" in graph_four:
      graph_four["color"] = graph4_color.replace("#", "")
 
   graph_five = graph_configurations[4]
   if "color" in graph_five:
      graph_five["color"] = graph5_color.replace("#", "")
     
 
 
   print(graph_one)
 
   
   
   
   print('graphname1', graph1_name)
   print('graphcolor1', graph1_color)
   print('graphname2', graph2_name)
   print('graphcolor2', graph2_color)
   print('graphname3', graph3_name)
   print('graphcolor3', graph3_color)
   print('graphname4', graph4_name)
   print('graphcolor4', graph4_color)
   print('graphname5', graph5_name)
   print('graphcolor5', graph5_color)
   return fastapi.responses.RedirectResponse(f'/page_5/?graph_configurations={graph_configurations}&graphtotal={graphtotal}&graph_type={graph_type}&url={url}', status_code=status.HTTP_302_FOUND)
 
###page 5
@app.get('/page_5', response_class=HTMLResponse)
async def get_fifth_form(request: Request, graphtotal: Union[int, None] = None, graph_type: Union[str, None] = None, graph_configurations: Union[str, None] = None, url: Union[str, None] = None):
   graph_configurations = ast.literal_eval(graph_configurations)
   create_multiple_graphs(url, graph_configurations)
   columnDisplayPage5(graphtotal)
 
   return templates.TemplateResponse("page5-results.html", {"request": request})  # returns form
   
 
# html needs to allow scroll
@app.post('/page_5', response_class=HTMLResponse)
async def post_first_form(request: Request, graphtotal: int = Form(...), csv_link: str = Form(...)):
    return fastapi.responses.RedirectResponse("page-5-results-html", {"request": request})
 
if __name__ == '__main__':
   # uvicorn.run(app, port=8080, host="0.0.0.0")
   uvicorn.run(app)