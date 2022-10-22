import uvicorn
import re
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, Request, Form, Depends, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sql_data import *
global csv_link
# from schemas import AwesomeForm  # uses schema file to bring in format of printing form data

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/page_1', response_class=HTMLResponse)
def get_basic_form(request: Request):
    return templates.TemplateResponse("page-1.html", {"request": request})  # renders HTML form and returns to user (lets us see the form)

@app.post('/page_1', response_class=HTMLResponse)
async def post_basic_form(request: Request, csv_link: str = Form(...)):
    print('CSV link:', csv_link)
    dbName(csv_link)
    return templates.TemplateResponse("page-1.html", {"request": request})  # returns form
if __name__ == '__main__':
    uvicorn.run(app)
