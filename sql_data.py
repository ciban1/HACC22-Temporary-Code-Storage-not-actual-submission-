import json
import urllib.request
import re
import fastapi
from app import *


def dbName(x):
     start = 'resource/'
     end = '/download'
     file_name = x[x.find(start) + len(start):x.rfind(end)]
     url = 'https://opendata.hawaii.gov/api/3/action/datastore_search_sql?sql=SELECT%20*%20from%20%22' + file_name + '%22%20'
     fileobj = urllib.request.urlopen(url)
     response_dict = json.loads(fileobj.read())
     print(response_dict)


