from turtle import right
import uvicorn
import re
from fastapi import FastAPI, Request, Form, Depends, UploadFile, File, Response 
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sql_data import *
from write_html2 import *
from backend.graph_functions import *
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route
from typing import List, Union

# from send_graph_to_dir import * # now in backend folder
global csv_link
# from schemas import AwesomeForm  # uses schema file to bring in format of printing form data

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# page 1
@app.get('/', response_class=HTMLResponse)
async def get_first_form(request: Request):
   return templates.TemplateResponse("page-1.html", {"request": request})  # returns form

@app.post('/', response_class=HTMLResponse)
async def post_first_form(request: Request, howmanyGraph: str = Form(...), csv_link: str = Form(...)):
   print('CSV link:', csv_link)
   print(howmanyGraph, 'graphs')
   # dbName(csv_link)
   column_list = str(column_headers(csv_link))
   print(type(column_list))
   #columnDisplayPage2(howmanyGraph)
   #put graph num and list in query param 
   urlb = app.url_path_for("get_second_form")
   url = f'{urlb}/?graphtotal={howmanyGraph}&headers={column_list}'#find number of column in column list, index the list using a
   return RedirectResponse(url)
   #return templates.TemplateResponse("page-1.html", {"request": request})  # returns form


##### page 2
@app.get('/page_2', response_class=HTMLResponse)
async def get_second_form(request: Request, graphtotal: Union[str, None] = None, headers: list[str, None] = None):
   print(graphtotal, headers)

   return templates.TemplateResponse("page2-results.html", {"request": request})


@app.post('/page_2', response_class=HTMLResponse)
def post_second_form(request: Request, column: list = Form(...), graph_type: list = Form(...), graphtotal: Union[str, None] = None, headers: Union[str, None] = None):  # array of selected columns; use position
   print(graphtotal)
   print(headers)
   import ast
   right_list = ast.literal_eval(headers)
   columnDisplayPage2(graphtotal, right_list)
   print(column)
   print(graph_type)
   return templates.TemplateResponse('page2-results.html', {'request': request})


@app.get('/page_5', response_class=HTMLResponse)
def get_graph(request: Request):
   # graph_display_test()  ### IMAGE NEEDS TO BE CREATED FROM POST OF PREVIOUS, OTHERWISE WILL NOT BE MADE IN TIME FOR HTML REQUEST
   return templates.TemplateResponse("graph-page.html", {"request": request})


if __name__ == '__main__':
   uvicorn.run(app)

