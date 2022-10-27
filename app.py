import uvicorn
import re
from fastapi import FastAPI, Request, Form, Depends, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sql_data import *
from write_html2 import *

# from send_graph_to_dir import * # now in backend folder
global csv_link
# from schemas import AwesomeForm  # uses schema file to bring in format of printing form data

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get_page2('/page_2', response_class=HTMLResponse)
def get_bruh(request: Request):
   return templates.TemplateResponse("page2-results.html", {"request": request})

@app.get_page1('/page_1', response_class=HTMLResponse)
def get_first_form(request: Request):
   return templates.TemplateResponse("page-1.html", {
       "request": request})  # renders HTML form and returns to user (lets us see the form)


@app.post('/page_1', response_class=HTMLResponse)
async def post_first_form(request: Request, howmanyGraph: str = Form(...), csv_link: str = Form(...)):
   print('CSV link:', csv_link)
   print(howmanyGraph, 'graphs')
   # dbName(csv_link)
   columnDisplayPage2(howmanyGraph)
#    return templates.TemplateResponse("page2-results.html", {"request": request})  # returns form
   get_page2()


##### page 2

'''jinja test'''



@app.post('/page_2', response_class=HTMLResponse)
def post_bruh(request: Request, column: list = Form(...), graph_type: list = Form(...)):  # array of selected columns; use position
   print(column)
   print(graph_type)
   # print(HTMLResponse)
   return templates.TemplateResponse('graph-page.html', {'request': request})




@app.get('/graph', response_class=HTMLResponse)
def get_graph(request: Request):
   # graph_display_test()  ### IMAGE NEEDS TO BE CREATED FROM POST OF PREVIOUS, OTHERWISE WILL NOT BE MADE IN TIME FOR HTML REQUEST
   return templates.TemplateResponse("graph-page.html", {"request": request})


if __name__ == '__main__':
   uvicorn.run(app)

