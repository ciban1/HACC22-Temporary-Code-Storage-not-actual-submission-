import json
import urllib.request
import pandas as pd

#File of data wanted
dataset_filename = "c65b9ca4-1124-423e-88bf-e81ab4afc8a1"

'''
Link to site: https://opendata.hawaii.gov/dataset/organizational-reports-for-hawaii-state-and-county-candidates/resource/df2c6524-8e85-47e5-bf04-20c43cc59c85
Pull link: https://opendata.hawaii.gov/api/3/action/datastore_search_sql?sql=SELECT * from "df2c6524-8e85-47e5-bf04-20c43cc59c85" LIMIT 10
* is all columns, specific column call by "Column name"
Remove where
Replace where with LIMIT #
from "database name"
'''

url1 = "https://opendata.hawaii.gov/api/3/action/datastore_search_sql?sql=SELECT%20*%20from%20%22df2c6524-8e85-47e5-bf04-20c43cc59c85%22%20LIMIT%2030"
fileobj = urllib.request.urlopen(url1)
response_dict = json.loads(fileobj.read())

#The results of the query
results_dict = response_dict["result"]

#The entire data set
dataset = response_dict["result"]['records']
# print("dataset", dataset)

#Fields list is a dictonary of headers and their types
fields_list = results_dict["fields"]

#return list of column headers
column_headers = []
for column_header in fields_list:
    column_headers.append(column_header["id"])
print("Column Headers", column_headers)

# Prints out all of the columns and their types
for column_header in fields_list:
  print("Column name: " + column_header["id"] + "; Data type: " + column_header["type"])

#Name of the column the user is requesting
column_one_name = 'Address 2'
column_two_name = 'District'
list_of_column_names = [column_one_name, column_two_name]

#Function to pull data of a column
def grab_column(column_to_pull):
 #print("Pulling", column_to_pull)
 #Hold the data
 column_data = []

 #The dataset is formatted as a list of all the rows
 for data_point in dataset:
     column_data.append(data_point[column_to_pull])
 print(column_data)
 return column_data

column_one = grab_column(column_one_name)
column_two = grab_column(column_two_name)

#Take the lists and make a data frame
df = pd.DataFrame({column_one_name:column_one, column_two_name:column_two})

#Data frame merging
#DataFrame_name.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)

#Shows the "none" data
# print(df.isnull())

#More cleaned blanks in data
purge = ''
for column in df:
#Check through the data frame to rebuild it with everything but blanks
    df = df[df[column].str[0:len(df)] != purge]
print("purge blanks", df)

#I think this is dropping what can't be converted and shifting the whole data set over
#Covert everything to numbers and purge everything that can't be converted to numbers
def convert_to_number(column_name):
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
convert_to_number((column_two_name))

# for column in column_header["type"]:
#     print(column)
#     print(is_numeric_dtype(df[column]))
#     if is_numeric_dtype(df[column]):
#         convert_to_number(column)

print("Change to numbers", df[column_two_name])

#drop all nulls
df = df.dropna()

#Cleaned clean dataset
print(df)

# for column_name in list_of_column_names:

column_one_array = df[column_two_name].to_numpy()
print(column_one_array)
