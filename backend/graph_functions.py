import matplotlib.pyplot as plt
import json
import urllib.request
import pandas as pd
import datetime
import geopandas as gpd
import numpy as np


# --------------------------------------------------- Files Functions --------------------------------------------------
def sql_query_link_converter(csv_url):
   before_file_name = 'resource/'  # Resource is right before the file name
   after_file_name = '/download'  # Download is right after the file name
   file_name = csv_url[csv_url.find(before_file_name) + len(before_file_name):csv_url.rfind(
       after_file_name)]  # Look right before and right after to find the file name in the csv link
   sql_query = 'https://opendata.hawaii.gov/api/3/action/datastore_search_sql?sql=SELECT%20*%20from%20%22' + file_name + '%22%20'  # SQL can query open data hawaii using the file name
   return sql_query


def grab_data_from_urls(url_list: list):
   df_to_concat = []
   for url in url_list:
       url = sql_query_link_converter(url)
       fileobj_one = urllib.request.urlopen(url)  # Grab from url
       response_dict = json.loads(fileobj_one.read())  # Load json
       dataset = response_dict["result"]['records']  # The entire data set
       df_to_concat.append(pd.DataFrame(dataset))
       concatted_df = pd.concat(df_to_concat)
   return concatted_df


def column_headers(url_list):
   df = grab_data_from_urls(url_list)
   all_column_headers = df.keys()
   # Add every column to the column headers list
   column_headers_list = []
   for column_header in all_column_headers:
       if "_" in column_header:
           pass
       else:
           column_headers_list.append(column_header)
   return column_headers_list


# save all created figures as "[graph type][graph id][time stamp].[file_type]"
def save_all_figures(file_type: str, figure_log):
   for figure in figure_log:
       time = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
       sub_directory_location = "graph_imgs/"
       figure["figure"].savefig(sub_directory_location + figure["type"] + str(figure["id"]) + "_" + time + "." + file_type)
       # "C:/Users/CClub/PycharmProjects/Pandas_Test"


# display figures for testing purposes only
def display_figures():
   plt.show()  # display all created figures


def grab_data_from_columns(values_dataframe, x_axis_name, y_axis_name):
   print(x_axis_name)
   print(y_axis_name)
   graph_df = pd.DataFrame({x_axis_name: values_dataframe[x_axis_name], y_axis_name: values_dataframe[y_axis_name]})

   graph_df = graph_df.dropna()  # Clean the dataframe of nulls

   # For every column that can be turned into number, change to numbers, else leave as is
   axis_name_list = [x_axis_name, y_axis_name]
   for axis_name in axis_name_list:
       try:
           graph_df[axis_name] = pd.to_numeric(graph_df[axis_name], errors="raise")
       except:
           pass

   # Grab the values from the dataframe
   x_values = graph_df[x_axis_name]
   y_values = graph_df[y_axis_name]
   return x_values, y_values


# --------------------------------------------- Displaying graphs functions --------------------------------------------

def generate_bar_graph(x_values, y_values, axis, color: str | None = None):
   axis.bar(x_values, y_values, color=color)


def generate_horizontal_bar_graph(x_values, y_values, axis, color: str | None = None):
   axis.barh(x_values, y_values, color=color)


def generate_line_graph(x_values, y_values, axis, color: str | None = None):
   sorted_x_values = x_values
   sorted_y_values = y_values

   if isinstance(x_values, list):
       if all(isinstance(x_value, (int, float)) for x_value in x_values):
           zipped_points = list(zip(tuple(x_values), tuple(y_values)))  # gets a list of (x,y) coordinates
           zipped_points.sort(key=lambda tup: tup[0])  # sorts list based on x-values of coordinates
           sorted_x_values = [tup[0] for tup in zipped_points]
           sorted_y_values = [tup[1] for tup in zipped_points]

   axis.plot(sorted_x_values, sorted_y_values, color=color)


def generate_scatter_plot(x_values, y_values, axis, color: str | None = None):
   axis.scatter(x_values, y_values, color=color)


def generate_pie_chart(data_values, axis, categories=None, colors=None):
   axis.pie(data_values, labels=categories, colors=colors)


def generate_geograph(longitude_values, latitude_values, axis, color: str | None = None,
                     x_axis_label: str | None = None, y_axis_label: str | None = None):
   world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
   world.plot(ax=axis)
   axis.set_xlim(-160, -154.6)
   axis.set_ylim(18.75, 22.4)
   if not x_axis_label:
       x_axis_label = "Longitude"
   if not y_axis_label:
       y_axis_label = "Latitude"

   axis.scatter(longitude_values, latitude_values, color=color)


def generate_histogram(data_values, axis, color: str | None = None):
   axis.hist(data_values, color=color, linewidth=0.5, edgecolor="white")


def create_graph(values_dataframe, axis, graph_id: int, graph_type: str, x_axis_name, y_axis_name,
                color: str | None = None, title: str | None = None, x_axis_label: str | None = None,
                y_axis_label: str | None = None, pie_colors=None):
   if isinstance(graph_type, list):
       for (single_graph_type, y_values) in zip(graph_type, y_axis_name):
           single_x_values, single_y_values = grab_data_from_columns(values_dataframe, x_axis_name, y_values)
           if single_graph_type == "bar":
               generate_bar_graph(
                   x_values=single_x_values,
                   y_values=single_y_values,
                   axis=axis
               )
           elif single_graph_type == "line":
               generate_line_graph(
                   x_values=single_x_values,
                   y_values=single_y_values,
                   axis=axis
               )
           elif single_graph_type == "scatter":
               generate_scatter_plot(
                   x_values=single_x_values,
                   y_values=single_y_values,
                   axis=axis
               )
           else:
               raise Exception("Graph type is not valid")

       graph_type = "multigraph"
   else:
       x_values, y_values = grab_data_from_columns(values_dataframe, x_axis_name, y_axis_name)
       if graph_type == "bar":
           generate_bar_graph(
               x_values=x_values,
               y_values=y_values,
               axis=axis,
               color=color
           )
       elif graph_type == "hbar":
           generate_horizontal_bar_graph(
               x_values=x_values,
               y_values=y_values,
               axis=axis,
               color=color
           )
       elif graph_type == "line":
           generate_line_graph(
               x_values=x_values,
               y_values=y_values,
               axis=axis,
               color=color
           )
       elif graph_type == "scatter":
           generate_scatter_plot(
               x_values=x_values,
               y_values=y_values,
               axis=axis,
               color=color
           )
       elif graph_type == "pie":
           generate_pie_chart(
               data_values=y_values,
               categories=x_values,
               axis=axis,
               colors=pie_colors
           )
       elif graph_type == "geo":
           generate_geograph(
               longitude_values=x_values,
               latitude_values=y_values,
               axis=axis,
               color=color
           )
       elif graph_type == "histogram":
           generate_histogram(
               data_values=x_values,
               axis=axis,
               color=color
           )
       else:
           raise Exception("Graph type is not valid")

   axis.set(xlabel=x_axis_label, ylabel=y_axis_label, title=title)
   return {"figure": axis.get_figure(), "type": graph_type, "id": graph_id}


def create_multiple_graphs(url, graph_count_string, graph_type_list, x_axis_column_name_list, y_axis_column_name_list,
                          color_list=None, title_list=None, x_axis_label_list=None, y_axis_label_list=None):
   # Create 5 different subplots to use
   fig1, ax1 = plt.subplots()
   fig2, ax2 = plt.subplots()
   fig3, ax3 = plt.subplots()
   fig4, ax4 = plt.subplots()
   fig5, ax5 = plt.subplots()
   logged_figures = []
   available_axes = [ax1, ax2, ax3, ax4, ax5]
   # Turn the graph count from a string to an int
   graph_count_number = int(graph_count_string)

   # For every graph that was requested to be made, make the graph
   for graph in range(graph_count_number):
       axis = available_axes.pop(0)
       graph_dictionary = create_graph(
           values_dataframe=grab_data_from_urls(url),
           axis=axis,
           graph_id=graph + 1,
           graph_type=graph_type_list[graph],
           x_axis_name=x_axis_column_name_list[graph],
           y_axis_name=y_axis_column_name_list[graph],
       )
       logged_figures.append(graph_dictionary)
       graph += 1

   save_all_figures("svg", logged_figures)
