# import json
# import urllib.request
# import pandas as pd
# import matplotlib.pyplot as plt
# import datetime
# import geopandas as gpd
#
#
# # Create multiple graphs, currently placeholder values for graph title and color
# def create_multiple_graphs(graph_count_string, graph_title="graph", graph_color="red"):
#     # Turn the graph count from a string to an int
#     graph_count_number = int(graph_count_string)
#
#     # For every graph that was requested to be made, make the graph
#     for graph in range(graph_count_number):
#         create_graph(
#             graph_type=graph_type_list[graph],
#             x_axis_name=x_axis_column_name_list[graph],
#             y_axis_name=y_axis_column_name_list[graph],
#             title=graph_title,
#             color=graph_color
#         )
#
#
# # Graph selector
# def create_graph(graph_type, x_axis_name, y_axis_name, title, color):
#     try:
#
#         axis_name_list = [x_axis_name, y_axis_name]
#         # create a dataframe of the columns in the graph
#         graph_df = pd.DataFrame({x_axis_name: entire_df[x_axis_name], y_axis_name: entire_df[y_axis_name]})
#
#         # Clean the dataframe of nulls
#         graph_df = graph_df.dropna()
#
#         # For every column that can be turned into number, change to numbers, else leave as is
#         for axis_name in axis_name_list:
#             try:
#                 graph_df[axis_name] = pd.to_numeric(graph_df[axis_name], errors="raise")
#             except:
#                 pass
#
#         # Grab the values from the dataframe
#         x_axis_values = graph_df[x_axis_name]
#         y_axis_values = graph_df[y_axis_name]
#
#         # Select type of graph
#         if graph_type == "bar":
#             create_bar_graph(
#                 x_values=x_axis_values,
#                 y_values=y_axis_values,
#                 color=color,
#                 title=title,
#                 x_axis_label=x_axis_name,
#                 y_axis_label=y_axis_name
#             )
#
#         if graph_type == "line":
#             create_line_graph(
#                 x=x_axis_values,
#                 y=y_axis_values,
#                 color=color,
#                 title=title,
#                 x_axis_label=x_axis_name,
#                 y_axis_label=y_axis_name
#             )
#
#         if graph_type == "scatter":
#             create_scatter_plot(
#                 x_values=x_axis_values,
#                 y_values=y_axis_values,
#                 color=color,
#                 title=title,
#                 x_axis_label=x_axis_name,
#                 y_axis_label=y_axis_name
#             )
#
#         if graph_type == "pie":
#             create_pie_chart(
#                 portion_values=y_axis_values,
#                 categories=x_axis_values,
#                 title=title
#             )
#
#         if graph_type == "geograph":
#             create_geograph(
#                 longitude_values=x_axis_values,
#                 latitude_values=y_axis_values,
#                 color=color,
#                 title=title
#             )
#     except:
#         # The graph could not be made
#         print("Something went wrong, try again")
#
#
# def create_bar_graph(x_values, y_values, color: str | None = None, title: str | None = None,
#                      x_axis_label: str | None = None, y_axis_label: str | None = None):
#     current_axis = available_axes.pop(0)
#     current_axis.bar(x_values, y_values, color=color)
#     current_axis.set(xlabel=x_axis_label, ylabel=y_axis_label, title=title)
#     logged_figures.append({"figure": current_axis.get_figure(), "type": "bargraph", "id": len(logged_figures) + 1})
#
#
# def create_line_graph(x: str, y: str, color: str | None = None, title: str | None = None,
#                       x_axis_label: str | None = None, y_axis_label: str | None = None):
#     sorted_x_points = x
#     sorted_y_points = y
#
#     if isinstance(x, list):
#         if all(isinstance(x_value, (int, float)) for x_value in x):
#             zipped_points = list(zip(tuple(x), tuple(y)))  # gets a list of (x,y) coordinates
#             zipped_points.sort(key=lambda tup: tup[0])  # sorts list based on x-values of coordinates
#             sorted_x_points = [tup[0] for tup in zipped_points]
#             sorted_y_points = [tup[1] for tup in zipped_points]
#
#     current_axis = available_axes.pop(0)
#     current_axis.plot(sorted_x_points, sorted_y_points, color=color)
#     current_axis.set(xlabel=x_axis_label, ylabel=y_axis_label, title=title)
#     logged_figures.append({"figure": current_axis.get_figure(), "type": "linegraph", "id": len(logged_figures) + 1})
#
#
# def create_scatter_plot(x_values, y_values, color: str | None = None, title: str | None = None,
#                         x_axis_label: str | None = None, y_axis_label: str | None = None):
#     current_axis = available_axes.pop(0)
#     current_axis.scatter(x_values, y_values, color=color)
#     current_axis.set(xlabel=x_axis_label, ylabel=y_axis_label, title=title)
#     logged_figures.append({"figure": current_axis.get_figure(), "type": "scatterplot", "id": len(logged_figures) + 1})
#
#
# def create_pie_chart(portion_values, categories=None, colors=None, title: str | None = None):
#     current_axis = available_axes.pop(0)
#     current_axis.pie(portion_values, labels=categories, colors=colors)
#     current_axis.set(title=title)
#     logged_figures.append({"figure": current_axis.get_figure(), "type": "piechart", "id": len(logged_figures) + 1})
#
#
# def create_geograph(longitude_values, latitude_values, color: str | None = None, title: str | None = None,
#                     x_axis_label: str | None = None, y_axis_label: str | None = None):
#     current_axis = available_axes.pop(0)
#     world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#     world.plot(ax=current_axis)
#     current_axis.set_xlim(-160, -154.6)
#     current_axis.set_ylim(18.75, 22.4)
#     if not x_axis_label:
#         x_axis_label = "Longitude"
#     if not y_axis_label:
#         y_axis_label = "Latitude"
#
#     current_axis.scatter(longitude_values, latitude_values, color=color)
#     current_axis.set(xlabel=x_axis_label, ylabel=y_axis_label, title=title)
#     logged_figures.append({"figure": current_axis.get_figure(), "type": "geograph", "id": len(logged_figures) + 1})
#
#
# def column_headers(url):
#     # create a list of column headers
#     # Grab from url
#     fileobj_one = urllib.request.urlopen(url)
#
#     # Load json
#     response_dict = json.loads(fileobj_one.read())
#
#     # The results of the query
#     results_dict = response_dict["result"]
#
#     # Fields list is a dictionary of headers and their types
#     fields_list = results_dict["fields"]
#
#     # Add every column to the column headers list
#     column_headers_list = []
#     for column_header in fields_list:
#         column_headers_list.append(column_header["id"])
#
#     return column_headers_list
#
#
# def grab_data_from_url(url):
#     # File of data wanted
#     dataset_filename = "c65b9ca4-1124-423e-88bf-e81ab4afc8a1"
#
#     # Grab from url
#     fileobj_one = urllib.request.urlopen(url)
#
#     # Load json
#     response_dict = json.loads(fileobj_one.read())
#
#     # The entire data set
#     dataset = response_dict["result"]['records']
#
#     # The entire data frame
#     entire_df = pd.DataFrame(dataset)
#     return entire_df
#
#
# def setup_graphs():
#     # figures for five graphs
#     fig1, ax1 = plt.subplots()
#     fig2, ax2 = plt.subplots()
#     fig3, ax3 = plt.subplots()
#     fig4, ax4 = plt.subplots()
#     fig5, ax5 = plt.subplots()
#     available_axes = [ax1, ax2, ax3, ax4, ax5]
#     return available_axes
#
#
# def graph_to_png():
#     # saves all created figures as "[graph type][graph id][time stamp].png"
#     for figure in logged_figures:
#         time = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
#         figure["figure"].savefig(figure["type"] + str(figure["id"]) + "_" + time + ".png")
#
#
# # Get data set to pull from front end
# url = 'https://opendata.hawaii.gov/api/3/action/datastore_search_sql?sql=SELECT%20*%20from%20%22158d4b5b-0b84-4f27-948e-6eb7a16131f4%22'  # dataset to pull from
#
# # Give the column header list to front end
# column_header_list = column_headers(url)
#
# # Receive the number of graph, type of graphs, x-axis columns, y-axis columns
# graph_count = "0"  # graph_count as string of number
# graph_type_list = []  # List of graph's types
# x_axis_column_name_list = []  # List of x axis column names
# y_axis_column_name_list = []  # List of x axis column names
#
# # Create a dataframe from all the columns
# entire_df = grab_data_from_url(url)  # big dataframe
#
# # Set up matplotlib to remember all the graphs created and have a separate figure for each graph
# logged_figures = []  # List of all the graphs
# available_axes = setup_graphs()  # New figure for each graph
#
# # Create many graphs based off the amount of graphs requested to be made
# create_multiple_graphs(graph_count_string=graph_count, graph_title="graph", graph_color="red")
#
# # Convert the graphs to a png
# graph_to_png()

import matplotlib.pyplot as plt
import json
import urllib.request
import pandas as pd
import datetime
import geopandas as gpd


# --------------------------------------------------- Files Functions --------------------------------------------------
def import_data_values(url: str, columns_to_pull):
   dataset_filename = "c65b9ca4-1124-423e-88bf-e81ab4afc8a1"  # file of data wanted
   fileobj_one = urllib.request.urlopen(url)  # grab from url
   response_dict = json.loads(fileobj_one.read())  # load json

   results_dict = response_dict["result"]  # the results of the query
   dataset = response_dict["result"]['records']  # the entire data set
   fields_list = results_dict["fields"]  # fields list is a dictionary of headers and their types
   column_headers_list = [column_header["id"] for column_header in fields_list]  # create a list of column headers
   dataset_columns = pd.DataFrame(dataset)  # take the data and make frame

   python_df = {}
   for column in columns_to_pull:
       python_df.update({column: dataset_columns[column]})
   graph_df = pd.DataFrame(python_df)  # create a dataframe of the columns in the graph
   graph_df = graph_df.dropna()  # clean the dataframe

   for column in graph_df:
       try:
           graph_df[column] = pd.to_numeric(graph_df[column], errors="raise")
       except:
           pass

   columns_generated = {}
   for column in graph_df:
       columns_generated.update({column: graph_df[column].tolist()})

   return columns_generated


# save all created figures as "[graph type][graph id][time stamp].[file_type]"
def save_all_figures(file_type: str):
   for figure in logged_figures:
       time = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
       figure["figure"].savefig(figure["type"] + str(figure["id"]) + "_" + time + "." + file_type)


# --------------------------------------------- Displaying graphs functions --------------------------------------------
# figures for five graphs
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()
fig5, ax5 = plt.subplots()
logged_figures = []
available_axes = [ax1, ax2, ax3, ax4, ax5]


def generate_bar_graph(x_values, y_values, color: str | None = None, title: str | None = None,
                      x_axis_label: str | None = None, y_axis_label: str | None = None, horizontal: bool = False):
   current_axis = available_axes.pop(0)

   if horizontal:
       current_axis.barh(x_values, y_values, color=color)
       current_axis.set(xlabel=y_axis_label, ylabel=x_axis_label, title=title)
       logged_figures.append(
           {"figure": current_axis.get_figure(), "type": "horizontalbargraph", "id": len(logged_figures) + 1})
   else:
       current_axis.bar(x_values, y_values, color=color)
       current_axis.set(xlabel=x_axis_label, ylabel=y_axis_label, title=title)
       logged_figures.append({"figure": current_axis.get_figure(), "type": "bargraph", "id": len(logged_figures) + 1})


def generate_line_graph(x_values, y_values, color: str | None = None, title: str | None = None,
                       x_axis_label: str | None = None, y_axis_label: str | None = None):
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


def generate_scatter_plot(x_values, y_values, color: str | None = None, title: str | None = None,
                         x_axis_label: str | None = None, y_axis_label: str | None = None):
   current_axis = available_axes.pop(0)

   current_axis.scatter(x_values, y_values, color=color)
   current_axis.set(xlabel=x_axis_label, ylabel=y_axis_label, title=title)
   logged_figures.append({"figure": current_axis.get_figure(), "type": "scatterplot", "id": len(logged_figures) + 1})


def generate_pie_chart(data_values, categories=None, colors=None, title: str | None = None):
   current_axis = available_axes.pop(0)
   current_axis.pie(data_values, labels=categories, colors=colors)
   current_axis.set(title=title)
   logged_figures.append({"figure": current_axis.get_figure(), "type": "piechart", "id": len(logged_figures) + 1})


def generate_geograph(longitude_values, latitude_values, color: str | None = None, title: str | None = None,
                     x_axis_label: str | None = None, y_axis_label: str | None = None):
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


def create_graph(graph_type: str, x_values, y_values, color: str | None = None, title: str | None = None,
                x_axis_label: str | None = None, y_axis_label: str | None = None, horizontal_bar: bool = False, pie_colors=None):

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
       generate_pie_chart(
           data_values=y_values,
           categories=x_values,
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


# --------------------------------------- Display graphs (testing purposes only) ---------------------------------------

def display_figures():
   for axis in available_axes:
       plt.close()  # prevent empty graphs from being displayed

   plt.show()  # display all created figures