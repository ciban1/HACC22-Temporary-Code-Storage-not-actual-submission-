import matplotlib.pyplot as plt
import json
import urllib.request
import pandas as pd
import datetime
import geopandas as gpd

# -------------------------------------------------- Importing Files --------------------------------------------------
dataset_filename = "c65b9ca4-1124-423e-88bf-e81ab4afc8a1"  # file of data wanted
url = 'https://opendata.hawaii.gov/api/3/action/datastore_search_sql?sql=SELECT%20*%20from%20%22158d4b5b-0b84-4f27' \
     '-948e-6eb7a16131f4%22'  # SQL Query dataset
fileobj_one = urllib.request.urlopen(url)  # grab from url
response_dict = json.loads(fileobj_one.read())  # load json

results_dict = response_dict["result"]  # the results of the query
dataset = response_dict["result"]['records']  # the entire data set
fields_list = results_dict["fields"]  # fields list is a dictionary of headers and their types
column_headers_list = [column_header["id"] for column_header in fields_list]  # create a list of column headers
entire_df = pd.DataFrame(dataset)  # take the data and make frame


# save all created figures as "[graph type][graph id][time stamp].[file_type]"
def save_all_figures(file_type: str):
   for figure in logged_figures:
       time = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
       figure["figure"].savefig(figure["type"] + str(figure["id"]) + "_" + time + "." + file_type)


# -------------------------------------------- Displaying graphs functions --------------------------------------------
# figures for five graphs
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()
fig5, ax5 = plt.subplots()
logged_figures = []
available_axes = [ax1, ax2, ax3, ax4, ax5]


def generate_bar_graph(x_values, y_values, color: str | None = None, title: str | None = None, x_axis_label: str | None = None, y_axis_label: str | None = None, horizontal: bool = False):
   current_axis = available_axes.pop(0)

   if horizontal:
       current_axis.barh(x_values, y_values, color=color)
       current_axis.set(xlabel=y_axis_label, ylabel=x_axis_label, title=title)
       logged_figures.append({"figure": current_axis.get_figure(), "type": "horizontalbargraph", "id": len(logged_figures) + 1})
   else:
       current_axis.bar(x_values, y_values, color=color)
       current_axis.set(xlabel=x_axis_label, ylabel=y_axis_label, title=title)
       logged_figures.append({"figure": current_axis.get_figure(), "type": "bargraph", "id": len(logged_figures) + 1})


def generate_line_graph(x_values, y_values, color: str | None = None, title: str | None = None, x_axis_label: str | None = None, y_axis_label: str | None = None):
   sorted_x_values = x_values
   sorted_y_values = y_values

   if isinstance(x_values, list):
       if all(isinstance(x_value, (int, float)) for x_value in x_values):
           zipped_points = list(zip(tuple(x_values), tuple(y_values)))  # gets a list of (x,y) coordinates
           zipped_points.sort(key=lambda tup: tup[0])  # sorts list based on x-values of coordinates
           sorted_x_values = [tup[0] for tup in zipped_points]
           sorted_y_values = [tup[1] for tup in zipped_points]

   current_axis = available_axes.pop(0)
   current_axis.plot(sorted_x_values, sorted_y_values, color=color)
   current_axis.set(xlabel=x_axis_label, ylabel=y_axis_label, title=title)
   logged_figures.append({"figure": current_axis.get_figure(), "type": "linegraph", "id": len(logged_figures) + 1})


def generate_scatter_plot(x_values, y_values, color: str | None = None, title: str | None = None, x_axis_label: str | None = None, y_axis_label: str | None = None):
   current_axis = available_axes.pop(0)

   current_axis.scatter(x_values, y_values, color=color)
   current_axis.set(xlabel=x_axis_label, ylabel=y_axis_label, title=title)
   logged_figures.append({"figure": current_axis.get_figure(), "type": "scatterplot", "id": len(logged_figures) + 1})


def generate_pie_chart(data_values, categories=None, colors=None, title: str | None = None):
   current_axis = available_axes.pop(0)
   current_axis.pie(data_values, labels=categories, colors=colors)
   current_axis.set(title=title)
   logged_figures.append({"figure": current_axis.get_figure(), "type": "piechart", "id": len(logged_figures) + 1})


def generate_geograph(longitude_values, latitude_values, color: str | None = None, title: str | None = None, x_axis_label: str | None = None, y_axis_label: str | None = None):
   current_axis = available_axes.pop(0)
   world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
   world.plot(ax=current_axis)
   current_axis.set_xlim(-160, -154.6)
   current_axis.set_ylim(18.75, 22.4)
   if not x_axis_label:
       x_axis_label = "Longitude"
   if not y_axis_label:
       y_axis_label = "Latitude"

   current_axis.scatter(longitude_values, latitude_values, color=color)
   current_axis.set(xlabel=x_axis_label, ylabel=y_axis_label, title=title)
   logged_figures.append({"figure": current_axis.get_figure(), "type": "geograph", "id": len(logged_figures) + 1})


def create_graph(graph_type: str, x, y, color: str | None = None, title: str | None = None, x_axis_label: str | None = None, y_axis_label: str | None = None, horizontal_bar: bool = False, pie_categories=None, pie_colors=None):
   if isinstance(y, list):
       graph_df = pd.DataFrame({x: entire_df[x]})  # create a dataframe of a column in the graph if y is a list (for pie chart)
   else:
       graph_df = pd.DataFrame({x: entire_df[x], y: entire_df[y]})  # create a dataframe of the columns in the graph

   graph_df = graph_df.dropna()  # clean the dataframe

   for dimension in [x, y]:
       try:
           graph_df[dimension] = pd.to_numeric(graph_df[dimension], errors="raise")
       except:
           pass

   x_values = graph_df[x].tolist()

   y_values = y
   if isinstance(y, str):
       y_values = graph_df[y].tolist()

   if graph_type == "bar":
       generate_bar_graph(
           x_values=x_values,
           y_values=y_values,
           color=color,
           title=title,
           x_axis_label=x_axis_label,
           y_axis_label=y_axis_label,
           horizontal=horizontal_bar
       )
   elif graph_type == "line":
       generate_line_graph(
           x_values=x_values,
           y_values=y_values,
           color=color,
           title=title,
           x_axis_label=x_axis_label,
           y_axis_label=y_axis_label
       )
   elif graph_type == "scatter":
       generate_scatter_plot(
           x_values=x_values,
           y_values=y_values,
           color=color,
           title=title,
           x_axis_label=x_axis_label,
           y_axis_label=y_axis_label
       )
   elif graph_type == "pie":
       if y_values:
           generate_pie_chart(
               data_values=x_values,
               categories=y_values,
               colors=pie_colors,
               title=title
           )
       else:
           generate_pie_chart(
               data_values=x_values,
               categories=pie_categories,
               colors=pie_colors,
               title=title
           )
   elif graph_type == "geo":
       generate_geograph(
           longitude_values=x_values,
           latitude_values=y_values,
           color=color,
           title=title,
           x_axis_label=x_axis_label,
           y_axis_label=y_axis_label
       )


# ------------------------------------------------- Graphs start here -------------------------------------------------

create_graph(
   graph_type="geo",
   x="longitude",
   y="latitude",
   color="red",
   title="Homeless Shelters in Hawaii"
)

create_graph(
   graph_type="pie",
   x="HIC Beds",
   title="Homeless Shelters in Hawaii",
   y="Organization"
)

# -------------------------------------------------- Graphs end here --------------------------------------------------

# save_all_figures("png")

# --------------------------------------- Display graphs (testing purposes only) ---------------------------------------
for axis in available_axes:
   plt.close()  # prevent empty graphs from being displayed

plt.show()  # display all created figures