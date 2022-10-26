import pandas as pd
import urllib
import json
print("Running Pandas version " + str(pd.__version__))

jsonFile = ''
df = pd.read_json(jsonFile)

print(df.to_string())

datasetFilename = ''

# Dataset on website: https://opendata.hawaii.gov/dataset/organizational-reports-for-hawaii-state-and-county-candidates/resource/df2c6524-8e85-47e5-bf04-20c43cc59c85
url1 = "https://opendata.hawaii.gov/api/3/action/datastore_search_sql?sql=SELECT%20*%20from%20%22df2c6524-8e85-47e5-bf04-20c43cc59c85%22"
fileobj = urllib.request.urlopen(url1)
responseDict = json.loads(fileobj.read)

results_dict = responseDict["result"]
print(responseDict)
