import matplotlib.pyplot as plt
import json
import urllib.request
import pandas as pd
import os


# --------------------------------------------------- Files Functions --------------------------------------------------
def sql_query_link_converter(csv_url):
    before_file_name = 'resource/'  # Resource is right before the file name
    after_file_name = '/download'  # Download is right after the file name
    if after_file_name in csv_url:
        file_name = csv_url[csv_url.find(before_file_name) + len(before_file_name):csv_url.rfind(
            after_file_name)]  # Look right before and right after to find the file name in the csv link
    else:
        file_name = csv_url[csv_url.find(before_file_name) + len(before_file_name):]
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
    return column_headers_list


def grab_data_from_urls(url):
    url = sql_query_link_converter(url)
    fileobj_one = urllib.request.urlopen(url)  # Grab from url
    response_dict = json.loads(fileobj_one.read())  # Load json
    dataset = response_dict["result"]['records']  # The entire data set
    # The entire data frame
    entire_df = pd.DataFrame(dataset)
    return entire_df


# save all created figures as "[graph type][graph id][time stamp].[file_type]"
def save_all_figures(file_type: str, figure_log):
    img_path = os.path.relpath(
        __file__)  # Figures out the relative path for you in case your working directory moves around.
    sub_directory_location = "../../"
    for figure in figure_log:
        figure["figure"].savefig(os.path.join(img_path, sub_directory_location + str(figure["id"]) + "." + file_type))


def grab_data_from_columns(values_dataframe, x_axis_name, y_axis_name):
    x_axis_name = x_axis_name.replace(" and ", " & ")
    y_axis_name = y_axis_name.replace(" and ", " & ")

    if x_axis_name == "enumerate":
        try:
            column_to_enumerate = pd.Series(values_dataframe[y_axis_name])
        except KeyError:
            raise Exception("A column could not be accessed because a column name did not exist in the data set")

        y_axis_values = column_to_enumerate.value_counts()
        x_axis_values = y_axis_values.index
        graph_df = pd.DataFrame({x_axis_name: x_axis_values, y_axis_name: y_axis_values})

        graph_df = graph_df.dropna()  # Clean the dataframe of nulls

    else:
        try:
            x_axis_values = values_dataframe[x_axis_name]
            y_axis_values = values_dataframe[y_axis_name]
        except KeyError:
            raise Exception("A column could not be accessed because a column name did not exist in the data set")
        graph_df = pd.DataFrame({x_axis_name: x_axis_values, y_axis_name: y_axis_values})

        graph_df = graph_df.dropna()  # Clean the dataframe of nulls
        axis_name_list = [x_axis_name, y_axis_name]
        for axis_name in axis_name_list:
            try:
                graph_df[axis_name] = pd.to_numeric(graph_df[axis_name], errors="raise")
            except:
                pass

    x_values = graph_df[x_axis_name]
    y_values = graph_df[y_axis_name]
    return x_values.to_list(), y_values.to_list()


# --------------------------------------------- Displaying graphs functions --------------------------------------------

def generate_bar_graph(x_values, y_values, axis, settings, legend_key):
    axis.bar(
        x_values,
        y_values,
        color=settings["color"],  # color of all bars, default blue
        label=legend_key
    )


def generate_line_graph(x_values, y_values, axis, settings, legend_key):
    sorted_x_values = x_values
    sorted_y_values = y_values

    if isinstance(x_values, list):
        if all(isinstance(x_value, (int, float)) for x_value in x_values):
            zipped_points = list(zip(tuple(x_values), tuple(y_values)))  # gets a list of (x,y) coordinates
            zipped_points.sort(key=lambda tup: tup[0])  # sorts list based on x-values of coordinates
            sorted_x_values = [tup[0] for tup in zipped_points]
            sorted_y_values = [tup[1] for tup in zipped_points]

    axis.plot(sorted_x_values,
              sorted_y_values,
              label=legend_key,
              color=settings["color"]
              )


def generate_scatter_plot(x_values, y_values, axis, settings, legend_key):
    axis.scatter(x_values,
                 y_values,
                 label=legend_key,
                 color=settings["color"])


def generate_pie_chart(data_values, axis, settings, labels):
    if not isinstance(settings["color"], list):
        default_color = ["red", "orange", "yellow", "green", "blue", "purple"]
        settings["color"] = default_color

    axis.pie(
        data_values,
        labels=labels,  # List of labels for each pie slice
        colors=settings["color"],  # List of colors for each pie slice, (custom) default rainbow

    )


def create_graph(values_dataframe, axis, graph_id: int, g_type, x_axis_name, y_axis_name, settings):
    for (single_g_type, single_y_axis_name, single_settings) in zip(g_type, y_axis_name,
                                                                                   settings):
        single_settings.update({"legend_key": single_y_axis_name})

        if "color" in single_settings:
            single_settings["color"] = "#" + single_settings["color"]
        else:
            default_color = "#000000"
            single_settings.update({"color": default_color})

        single_x_values, single_y_values = grab_data_from_columns(values_dataframe, x_axis_name,
                                                                  single_y_axis_name)
        if single_g_type == "Bar Graph":
            generate_bar_graph(
                x_values=single_x_values,
                y_values=single_y_values,
                axis=axis,
                settings=single_settings,
                legend_key=single_settings["legend_key"]
            )
        elif single_g_type == "Line Graph":
            generate_line_graph(
                x_values=single_x_values,
                y_values=single_y_values,
                axis=axis,
                settings=single_settings,
                legend_key=single_settings["legend_key"]
            )
        elif single_g_type == "Scatter Graph":
            generate_scatter_plot(
                x_values=single_x_values,
                y_values=single_y_values,
                axis=axis,
                settings=single_settings,
                legend_key=single_settings["legend_key"]
            )
        elif single_g_type == "Pie Graph":
            if "labels" not in single_settings:
                single_settings.update({"labels": single_x_values})
            generate_pie_chart(
                data_values=single_y_values,
                axis=axis,
                settings=single_settings,
                labels=single_settings["labels"]
            )
        else:
            raise Exception("Graph type is not valid for multi-graphing. Please input 'Bar Graph', 'Line Graph', "
                            "'Pie Graph', or 'Scatter Graph'.")

    graph_dictionary = {"figure": axis.get_figure(), "id": graph_id}

    return graph_dictionary


def create_multiple_graphs(urls, graph_configurations):
    if not (isinstance(graph_configurations, list) and all(
            isinstance(graph_configuration, dict) for graph_configuration in graph_configurations)):
        raise Exception("graph_configurations must be a list of dictionaries")

    if len(graph_configurations) > 5:
        raise Exception(f"You may only graph up to five graphs at a time with create_multiple_graphs.  You are trying "
                        f"to graph {len(graph_configurations)} graphs")

    # Create 5 different subplots to use
    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig3, ax3 = plt.subplots()
    fig4, ax4 = plt.subplots()
    fig5, ax5 = plt.subplots()
    logged_figures = []
    available_axes = [ax1, ax2, ax3, ax4, ax5]
    # Turn the graph count from a string to an int
    graph_count_number = len(graph_configurations)

    # For every graph that was requested to be made, make the graph
    for graph in range(graph_count_number):

        if "g_type" not in graph_configurations[graph]:
            pass
        else:
            axis = available_axes.pop(0)
            graph_dictionary = create_graph(
                values_dataframe=grab_data_from_urls(urls),
                axis=axis,
                graph_id=graph + 1,
                g_type=graph_configurations[graph]["g_type"],
                x_axis_name=graph_configurations[graph]["x_axis_name"],
                y_axis_name=graph_configurations[graph]["y_axis_name"],
                settings=graph_configurations[graph]["settings"],
            )
            logged_figures.append(graph_dictionary)

    save_all_figures("svg", logged_figures)


def display_created_figures():
    plt.show()  # displaying graphs for testing purposes only
