import matplotlib.pyplot as plt
import json
import urllib.request
import pandas as pd
import datetime
import geopandas as gpd


# --------------------------------------------------- Files Functions --------------------------------------------------
def sql_query_link_converter(csv_url):
    before_file_name = 'resource/'  # Resource is right before the file name
    after_file_name = '/download'  # Download is right after the file name
    file_name = csv_url[csv_url.find(before_file_name) + len(before_file_name):csv_url.rfind(
        after_file_name)]  # Look right before and right after to find the file name in the csv link
    sql_query = 'https://opendata.hawaii.gov/api/3/action/datastore_search_sql?sql=SELECT%20*%20from%20%22' + file_name + '%22%20'  # SQL can query open data hawaii using the file name
    return sql_query


def column_headers(url):
    # create a list of column headers
    url = sql_query_link_converter(url)  # Convert the csv url to a sql query
    fileobj_one = urllib.request.urlopen(url)  # Grab from url
    response_dict = json.loads(fileobj_one.read())  # Load json
    results_dict = response_dict["result"]  # The results of the query
    fields_list = results_dict["fields"]  # Fields list is a dictionary of headers and their types
    # Add every column to the column headers list
    column_headers_list = []
    for column_header in fields_list:
        if "_" in column_header["id"]:
            pass
        else:
            column_headers_list.append(column_header["id"])
    print(column_headers_list)
    return column_headers_list

def grab_data_from_url(url):
    url = sql_query_link_converter(url)
    fileobj_one = urllib.request.urlopen(url)  # Grab from url
    response_dict = json.loads(fileobj_one.read())  # Load json
    dataset = response_dict["result"]['records']  # The entire data set
    # The entire data frame
    entire_df = pd.DataFrame(dataset)
    return entire_df


# save all created figures as "[graph type][graph id][time stamp].[file_type]"
def save_all_figures(file_type: str):
    for figure in logged_figures:
        time = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        figure["figure"].savefig(figure["type"] + str(figure["id"]) + "_" + time + "." + file_type)


# --------------------------------------------- Displaying graphs functions --------------------------------------------
def create_subplots():
    global logged_figures
    global available_axes
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


def create_graph(values_dataframe, graph_type: str, x_axis_name, y_axis_name, color: str | None = None,
                 title: str | None = None,
                 x_axis_label: str | None = None, y_axis_label: str | None = None, horizontal_bar: bool = False,
                 pie_colors=None):
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


def create_multiple_graphs(url, graph_count_string, graph_type_list, x_axis_column_name_list, y_axis_column_name_list):
    # Create 5 different subplots to use
    create_subplots()
    # Turn the graph count from a string to an int
    graph_count_number = int(graph_count_string)

    # For every graph that was requested to be made, make the graph
    for graph in range(graph_count_number):
        create_graph(
            values_dataframe=grab_data_from_url(url),
            graph_type=graph_type_list[graph],
            x_axis_name=x_axis_column_name_list[graph],
            y_axis_name=y_axis_column_name_list[graph]
        )


# --------------------------------------- Display graphs (testing purposes only) ---------------------------------------

def display_figures():
    for axis in available_axes:
        plt.close()  # prevent empty graphs from being displayed

    plt.show()  # display all created figures
