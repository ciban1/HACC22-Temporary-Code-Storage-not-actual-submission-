from graph_functions import create_multiple_graphs, column_headers

url_list = ["https://opendata.hawaii.gov/dataset/607c1121-5c0b-473f-a95f-22bca7f89c5a/resource/bf4fd6d1-a58a-4c4e-91ca-5d4d467f4dc3/download/homeless_students_in_public_school.csv"]
print(column_headers(url_list))
create_multiple_graphs(
  urls=url_list,
  graph_configurations=[{
      "graph_type": "pie",
      "x_axis_name": "Hotels or Motels",
      "y_axis_name": "Shelters, transitional housing, or awaiting foster care placeme",
      "polar": False,
      "settings": {}},
      {
       "graph_type": "pie",
      "x_axis_name": "Hotels or Motels",
      "y_axis_name": "Unsheltered",
      "polar": False,
      "settings": {}
      }]
)
