import uvicorn
import re
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, Request, Form, Depends, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sql_data import *
from write_html2 import *
from send_graph_to_dir import *
global csv_link
# from schemas import AwesomeForm  # uses schema file to bring in format of printing form data

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/page_1', response_class=HTMLResponse)
def get_first_form(request: Request):
   return templates.TemplateResponse("page-1.html", {"request": request})  # renders HTML form and returns to user (lets us see the form)

@app.post('/page_1', response_class=HTMLResponse)
async def post_first_form(request: Request, howmanyGraph: str = Form(...), csv_link: str = Form(...)):
   print('CSV link:', csv_link)
   print(howmanyGraph, 'graphs')
   dbName(csv_link)
   columnDisplayPage2(howmanyGraph)
   return templates.TemplateResponse("page-1.html", {"request": request})  # returns form
##### page 2

'''jinja test'''

@app.get('/bruh', response_class=HTMLResponse)
def get_bruh(request: Request):
   return templates.TemplateResponse("page2-results.html", {"request":request})

@app.post('/bruh', response_class=HTMLResponse)
def post_bruh(request: Request, graph_column_select = Form(...)):
   print(graph_column_select)

   return templates.TemplateResponse('page2-results.html', {'request': request})

# page 2 stuff (above is test)
''''''''''''''''''''''''''''''''''''''''''''''''
@app.get('/page_2', response_class=HTMLResponse)
def get_second_form(request: Request):
   return templates.TemplateResponse("page-2.html", {"request":request})

@app.post('/page_2', response_class=HTMLResponse)
def post_second_form(request: Request, graphNum: str = Form(...), graphType: str = Form(...), checkbox_column1: bool = Form(False), checkbox_column2: bool = Form(False), checkbox_column3: bool = Form(False), checkbox_column4: bool = Form(False), checkbox_column5: bool = Form(False)):
   print('Graph Number', graphNum)
   print('Graph Type', graphType)
   print('CheckBoxColumn1', checkbox_column1)
   print('CheckBoxColumn2', checkbox_column2)
   print('CheckBoxColumn3', checkbox_column3)
   print('CheckBoxColumn4', checkbox_column4)
   print('CheckBoxColumn5', checkbox_column5)
   return templates.TemplateResponse('page-2.html', {'request': request})
   # async def post_second_form(request: Request, csv_link: str = Form(...)):
   # return templates.TemplateResponse("page-1.html", {"request": request})  # returns form


@app.get('/graph', response_class=HTMLResponse)
def get_graph(request: Request):
   graph_display_test()  ### IMAGE NEEDS TO BE CREATED FROM POST OF PREVIOUS, OTHERWISE WILL NOT BE MADE IN TIME FOR HTML REQUEST
   return templates.TemplateResponse("graph-page.html", {"request":request})


if __name__ == '__main__':
   uvicorn.run(app)