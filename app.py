from turtle import right
from urllib.request import HTTPPasswordMgrWithDefaultRealm
import uvicorn
import re
from fastapi import FastAPI, Request, Form, Depends, UploadFile, File, Response
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sql_data import *
from write_html2 import *
from write_html3 import *
from write_html5 import *
from backend.graph_functions import *
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route
from typing import List, Union
import ast
import starlette.status as status


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


# html needs to allow scroll
@app.post('/', response_class=HTMLResponse)
async def post_first_form(request: Request, graphtotal: int = Form(...), csv_link: str = Form(...)):
    print('CSV link:', csv_link)
    print(graphtotal, 'graphs')
    # column_list = (column_headers(csv_link))
    column_list = str(column_headers(csv_link)).replace("&", "and")
    print(column_list)

    # put graph num and list in query param
    # urlb = app.url_path_for("get_second_form")
    # url = f'{urlb}/?graphtotal={graphtotal}&headers={headers}'#find number of column in column list, index the list using a
    # return RedirectResponse(url)
    return fastapi.responses.RedirectResponse(f'/page_2/?graphtotal={graphtotal}&headers={column_list}',
                                              status_code=status.HTTP_302_FOUND)


##### page 2
@app.get('/page_2', response_class=HTMLResponse)
async def get_second_form(request: Request, graphtotal: Union[int, None] = None, headers: Union[str, None] = None):
    print("from get 2", graphtotal, headers)
    right_list = ast.literal_eval(headers)
    print(right_list)

    columnDisplayPage2(graphtotal, right_list)
    return templates.TemplateResponse("page2-results.html", {"request": request})


@app.post('/page_2', response_class=HTMLResponse)
def post_second_form(request: Request, column: list = Form(...), graph_type: list = Form(...),
                     graphtotal: Union[str, None] = None,
                     headers: Union[str, None] = None):  # array of selected columns; use position
    print(column)
    print(graph_type)
    headers1 = []
    headers2 = []
    headers3 = []
    headers4 = []
    headers5 = []
    count = 1
    while count < (int(graphtotal) + 1):
        for i in column:
            for char in i:
                if char == "1":
                    if i not in headers1:
                        headers1.append(i)
                elif char == "2":
                    if i not in headers2:
                        headers2.append(i)
                elif char == "3":
                    if i not in headers3:
                        headers3.append(i)
                elif char == "4":
                    if i not in headers4:
                        headers4.append(i)
                elif char == "5":
                    if i not in headers5:
                        headers5.append(i)
        count = count + 1
    print(headers1)
    print(headers2)
    print(headers3)
    print(headers4)
    print(headers5)
    return fastapi.responses.RedirectResponse(f'/page_3', status_code=status.HTTP_302_FOUND)


# ### page 3
@app.get('/page_3', response_class=HTMLResponse)
async def get_third_form(request: Request, graphtotal: Union[str, None] = None, headers1: list[str, None] = None,
                         headers2: list[str, None] = None):
    graphtotal = 3
    headers1 = ['County1', 'Date1']
    headers2 = ['Urban Land Percentage2', 'Date2']
    headers3 = ['Urban Land Percentage3', 'Date3']
    headers4 = ['Urban Land Percentage4', 'Date4']
    headers5 = []
    graph_count = [1, 2, 3, 4]
    columnDisplayPage3(graphtotal, headers1, headers2, headers3, headers4, headers5)
    return templates.TemplateResponse("page3-results.html", {"request": request})

    # return templates.TemplateResponse("page2-results.html", {"request": request})


@app.post('/page_3', response_class=HTMLResponse)
def post_third_form(request: Request):
    pass


# page 5
@app.get('/page_5', response_class=HTMLResponse)
async def get_fifth_form(request: Request, graphtotal: Union[str, None] = None):
    graphtotal = 2
    columnDisplayPage5(graphtotal)
    return templates.TemplateResponse("page5-results.html", {"request": request})  # returns form

# html needs to allow scroll
@app.post('/page_5', response_class=HTMLResponse)
async def post_first_form(request: Request, graphtotal: int = Form(...), csv_link: str = Form(...)):
    return fastapi.responses.RedirectResponse("page-5-results-html", {"request": request})


# '''dont touch'''

# @app.post('/page_2', response_class=HTMLResponse)
# def post_second_form(request: Request, column: list = Form(...), graph_type: list = Form(...), graphtotal: Union[str, None] = None, headers: Union[str, None] = None):  # array of selected columns; use position
#    # urlb = app.url_path_for("get_second_form")
#    # url = f'{urlb}/?graphtotal={graphtotal}&headers={headers}headers1={headers1}&headers2={headers2}&headers3={headers3}&headers4={headers4}&headers5={headers5}'#find number of column in column list, index the list using a

#    print(graphtotal)
#    print(headers)
#    right_list = ast.literal_eval(headers)
#    columnDisplayPage2(graphtotal, right_list)
#    print(column)
#    print(graph_type)
#    headers1 = []
#    headers2 = []
#    headers3 = []
#    headers4 = []
#    headers5 = []
#    count = 1
#    while count < (int(graphtotal) + 1):
#       for i in column:
#          for char in i:
#             if char == "1":
#                if i not in headers1:
#                   headers1.append(i)
#                   break
#             elif char == "2":
#                if i not in headers2:
#                   headers2.append(i)
#             elif char == "3":
#                if i not in headers3:
#                   headers3.append(i)
#             elif char == "4":
#                if i not in headers4:
#                   headers4.append(i)
#             elif char == "5":
#                if i not in headers5:
#                   headers5.append(i)
#       count = count + 1
#    print(headers1)
#    print(headers2)
#    print(headers3)
#    print(headers4)
#    print(headers5)
#    return templates.TemplateResponse("page2-results.html", {"request": request})
#    # store each list of headers1-5 in url


# # ### page 3
# @app.get('/page_3', response_class=HTMLResponse)
# async def get_third_form(request: Request, graphtotal: Union[str, None] = None, headers1: list[str, None] = None, headers2: list[str, None] = None):
#    print(graphtotal, headers1)

#    # return templates.TemplateResponse("page2-results.html", {"request": request})

# # @app.post('/page_3', response_class=HTMLResponse)
# # def post_third_form(request: Request):


# ### page 5

# @app.get('/page_5', response_class=HTMLResponse)
# def get_graph(request: Request):
#    # graph_display_test()  ### IMAGE NEEDS TO BE CREATED FROM POST OF PREVIOUS, OTHERWISE WILL NOT BE MADE IN TIME FOR HTML REQUEST
#    return templates.TemplateResponse("graph-page.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run(app)
