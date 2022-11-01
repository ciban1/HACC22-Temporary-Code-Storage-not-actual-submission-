from glob import glob
import matplotlib.pyplot as plt
import json
import urllib.request
import pandas as pd
import datetime
import geopandas as gpd
import os
 
# # save all created figures as "[graph type][graph id][time stamp].[file_type]"
# def save_all_figures(file_type: str, figure_log):
#    for figure in figurelog:
#        time = datetime.datetime.now().strftime("%y%m%d%H%M%S")
#        sub_directory_location = "/graph_imgs/"
#        figure["figure"].savefig(sub_directorylocation + figure["type"] + str(figure["id"]) + "" + time + "." + file_type)
#        # "C:/Users/CClub/PycharmProjects/Pandas_Test"
 
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
    img_path = os.path.relpath(__file__)  # Figures out the absolute path for you in case your working directory moves around.
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
    if "color" not in settings:
        default_color = "blue"
        settings.update({"color": default_color})
    if "edge_color" not in settings:
        default_edge_color = "blue"
        settings.update({"edge_color": default_edge_color})
    if "edge_weight" not in settings:
        settings.update({"edge_weight": 0})
    if "bar_width" not in settings:
        settings.update({"bar_width": 0.8})
    if "align" not in settings:
        settings.update({"align": "center"})
 
    axis.bar(
        x_values,
        y_values,
        color=settings["color"],  # color of all bars, default blue
        width=settings["bar_width"],  # width of all bars, default 0.8
        edgecolor=settings["edge_color"],  # edge color of all bars, default blue
        linewidth=settings["edge_weight"],  # edge thickness, default 0 (no edge)
        align=settings["align"],
        # x-alignment of the bars; 'center' is default, 'edge' aligns the left edge of the bars with x-positions
        # to align right edges with x-positions, input 'edge' and a negative bar_width
        label=legend_key
    )
 
 
def generate_horizontal_bar_graph(x_values, y_values, axis, settings, legend_key):
    if "color" not in settings:
        default_color = "blue"
        settings.update({"color": default_color})
    if "edge_color" not in settings:
        default_edge_color = "blue"
        settings.update({"edge_color": default_edge_color})
    if "edge_weight" not in settings:
        settings.update({"edge_weight": 0})
    if "bar_width" not in settings:
        settings.update({"bar_width": 0.8})
    if "align" not in settings:
        settings.update({"align": "center"})
 
    axis.barh(
        x_values,
        y_values,
        color=settings["color"],  # color of all bars, default blue
        height=settings["bar_width"],  # width of all bars, default 0.8
        edgecolor=settings["edge_color"],  # edge color of all bars, default blue
        linewidth=settings["edge_weight"],  # edge thickness, default 0.8
        align=settings["align"],
        # y-alignment of the bars; 'center' is default, 'edge' aligns the bottom edge of the bars with y-positions
        # to align top edges with y-positions, input 'edge' and a negative bar_width
        label=legend_key
    )
 
 
def generate_line_graph(x_values, y_values, axis, settings, legend_key):
    sorted_x_values = x_values
    sorted_y_values = y_values
    if "color" not in settings:
        default_color = "blue"
        settings.update({"color": default_color})
 
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
    if "color" not in settings:
        default_color = "blue"
        settings.update({"color": default_color})
 
    axis.scatter(x_values,
                 y_values,
                 label=legend_key,
                 color=settings["color"])
 
 
def generate_pie_chart(data_values, axis, settings, labels):
    if "color" not in settings:
        default_color = ["red", "orange", "yellow", "green", "blue", "purple"]
        settings.update({"color": default_color})
    if "explode" not in settings:
        settings.update({"explode": [0 for i in range(len(data_values))]})
    if "label_in_slice" not in settings:
        settings.update({"label_in_slice": None})
    if "distance_from_label_in_slice_to_center" not in settings:
        settings.update({"distance_from_label_in_slice_to_center": 0.6})
    if "shadow" not in settings:
        settings.update({"shadow": False})
    if "label_distance_from_edge" not in settings:
        settings.update({"label_distance_from_edge": 1.1})
    if "start_angle" not in settings:
        settings.update({"start_angle": 0})
    if "radius" not in settings:
        settings.update({"radius": 1})
    if "counterclockwise_rotation" not in settings:
        settings.update({"counterclockwise_rotation": True})
    if "center_location" not in settings:
        settings.update({"center_location": (0, 0)})
    if "frame" not in settings:
        settings.update({"frame": False})
    if "rotate_labels_to_match_edge" not in settings:
        settings.update({"rotate_labels_to_match_edge": False})
 
    axis.pie(
        data_values,
        labels=labels,  # List of labels for each pie slice
        colors=settings["color"],  # List of colors for each pie slice, (custom) default rainbow
        explode=settings["explode"],  # List of distances wedge is away from center, default none
        autopct=settings["label_in_slice"],
        # The label within the slices. "%[distance_away_from_center].[amount_of_digits]%% for percent", default none
        pctdistance=settings["distance_from_label_in_slice_to_center"],
        # Distance label within slice is away from the center, default 0.6
        shadow=settings["shadow"],  # Shadow on or off, default False
        labeldistance=settings["label_distance_from_edge"],
        # Distance of the outside labels from the edge of the pie graph, default 1.1
        startangle=settings["start_angle"],  # Change the start angle, default 0
        radius=settings["radius"],  # Size of the graph, default 1
        counterclock=settings["counterclockwise_rotation"],  # Change to rotate clockwise, default True
        center=settings["center_location"],  # Change the center location, default(0,0)
        frame=settings["frame"],  # Have the graph be framed with x and y axes, default False
        rotatelabels=settings["rotate_labels_to_match_edge"]
        # Rotate the outside labels to match with the graph, default False
 
    )
 
    if "donut_hole" in settings:
        donut_hole = plt.Circle(xy=settings["donut_hole"]["donut_hole_location"],
                                radius=settings["donut_hole"]["donut_hole_size"],
                                color=settings["donut_hole"]["donut_hole_color"])
        axis.add_artist(donut_hole)
 
 
def generate_geograph(longitude_values, latitude_values, axis, settings, legend_key):
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world.plot(ax=axis)
    axis.set_xlim(-160, -154.6)
    axis.set_ylim(18.75, 22.4)
    if "color" not in settings:
        default_color = "blue"
        settings.update({"color": default_color})
 
    axis.scatter(longitude_values,
                 latitude_values,
                 label=legend_key,
                 color=settings["color"])
 
 
def generate_histogram(data_values, axis, settings, legend_key):
    if "color" not in settings:
        default_color = "blue"
        settings.update({"color": default_color})
    axis.hist(data_values,
              label=legend_key,
              color=settings["color"])
 
 
def create_graph(values_dataframe, axis, graph_id: int, g_type, x_axis_name, y_axis_name, settings,
                 x_axis_label, y_axis_label, title, x_data, y_data, show_legend, x_range, y_range,
                 x_axis_label_font_name, y_axis_label_font_name, title_font_name, x_axis_label_font_size,
                 y_axis_label_font_size, title_font_size):
    if isinstance(g_type, list):
        if not (isinstance(y_axis_name, list) and len(y_axis_name) >= len(g_type)):
            raise Exception("y_axis_name is not of proper length for multi-graphing.  Make sure y_axis_name is a "
                            "list and of equal length to g_type")
        if not (isinstance(settings, list) and len(settings) >= len(g_type)):
            raise Exception("settings is not of proper length for multi-graphing.  Make sure settings is a list and of "
                            "equal length to g_type.")
 
        if not x_data:
            x_data = [None for i in range(len(g_type))]
        if not y_data:
            y_data = [None for i in range(len(g_type))]
 
        y_values = []
        for (single_g_type, single_y_axis_name, single_settings, single_y_data) in zip(g_type, y_axis_name,
                                                                                           settings, y_data):
            if "legend_key" not in single_settings:
                single_settings.update({"legend_key": single_y_axis_name})
            if all(x_data_point is not None for x_data_point in x_data) and all(
                    y_data_point is not None for y_data_point in y_data):
                single_x_values = x_data
                single_y_values = single_y_data
            else:
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
                raise Exception("Graph type is not valid for multi-graphing. Please input 'bar', 'line', 'pie', "
                                "or 'scatter'.")
            y_values.append(single_y_values)
            x_values = single_x_values
        graph_dictionary = {"figure": axis.get_figure(), "type": "multigraph", "id": graph_id}
    else:
        if "legend_key" not in settings:
            settings.update({"legend_key": y_axis_name})
        if x_data and y_data:
            x_values = x_data
            y_values = y_data
        else:
            x_values, y_values = grab_data_from_columns(values_dataframe, x_axis_name, y_axis_name)
        if g_type == "Bar Graph":
            generate_bar_graph(
                x_values=x_values,
                y_values=y_values,
                axis=axis,
                settings=settings,
                legend_key=settings["legend_key"]
            )
        elif g_type == "hbar":
            generate_horizontal_bar_graph(
                x_values=y_values,
                y_values=x_values,
                axis=axis,
                settings=settings,
                legend_key=settings["legend_key"]
            )
        elif g_type == "Line Graph":
            generate_line_graph(
                x_values=x_values,
                y_values=y_values,
                axis=axis,
                settings=settings,
                legend_key=settings["legend_key"]
            )
        elif g_type == "Scatter Graph":
            generate_scatter_plot(
                x_values=x_values,
                y_values=y_values,
                axis=axis,
                settings=settings,
                legend_key=settings["legend_key"]
            )
        elif g_type == "Pie Graph":
            if "labels" not in settings:
                settings.update({"labels": x_values})
            generate_pie_chart(
                data_values=y_values,
                axis=axis,
                settings=settings,
                labels=x_values
            )
        elif g_type == "geo":
            if not x_axis_label:
                x_axis_label = "Longitude"
            if not y_axis_label:
                y_axis_label = "Latitude"
            generate_geograph(
                longitude_values=x_values,
                latitude_values=y_values,
                axis=axis,
                settings=settings,
                legend_key=settings["legend_key"]
            )
        elif g_type == "histogram":
            generate_histogram(
                data_values=y_values,
                axis=axis,
                settings=settings,
                legend_key=settings["legend_key"]
            )
        else:
            raise Exception(
                "Graph type is not valid. Please input 'bar', 'hbar', 'line', 'scatter', 'pie', 'geo', or 'histogram'.")
 
        graph_dictionary = {"figure": axis.get_figure(), "type": g_type, "id": graph_id}
 
    if show_legend:
        axis.legend()
 
    axis.set_xlabel(x_axis_label, fontname=x_axis_label_font_name, fontsize=x_axis_label_font_size)
    axis.set_ylabel(y_axis_label, fontname=y_axis_label_font_name, fontsize=y_axis_label_font_size)
    axis.set_title(title, fontname=title_font_name, fontsize=title_font_size)
 
    if not x_range:
        x_range = list(axis.get_xlim())
    if not y_range:
        y_range = list(axis.get_ylim())
 
    axis.set_xlim(x_range)
    axis.set_ylim(y_range)
 
    graph_configuration = {
        "g_type": g_type,
        "x_axis_name": x_axis_name,
        "y_axis_name": y_axis_name,
        "title": title,
        "x_axis_label": x_axis_label,
        "y_axis_label": y_axis_label,
        "settings": settings,
        "x_data": x_values,
        "y_data": y_values,
        "show_legend": show_legend,
        "x_range": x_range,
        "y_range": y_range,
        "x_axis_label_font_name": x_axis_label_font_name,
        "y_axis_label_font_name": y_axis_label_font_name,
        "title_font_name": title_font_name,
        "x_axis_label_font_size": x_axis_label_font_size,
        "y_axis_label_font_size": y_axis_label_font_size,
        "title_font_size": title_font_size
    }
    #plt.setp(axis.get_xticklabels(), rotation=30, horizontalalignment='right')
    return graph_dictionary, graph_configuration
 
 
def create_multiple_graphs(urls, graph_configurations):
    if not (isinstance(graph_configurations, list) and all(
            isinstance(graph_configuration, dict) for graph_configuration in graph_configurations)):
        raise Exception("graph_configurations must be a list of dictionaries")
 
    if len(graph_configurations) > 5:
        raise Exception(f"You may only graph up to five graphs at a time with create_multiple_graphs.  You are trying "
                        f"to graph {len(graph_configurations)} graphs")
 
    polar_options = []
    for graph_number in range(5):
        if graph_number < len(graph_configurations):
            if "polar" not in graph_configurations[graph_number]:
                graph_configurations[graph_number].update({"polar": False})
            polar_options.append(graph_configurations[graph_number]["polar"])
        else:
            polar_options.append(False)
 
    # Create 5 different subplots to use
    fig1, ax1 = plt.subplots(subplot_kw=dict(polar=polar_options[0]))
    fig2, ax2 = plt.subplots(subplot_kw=dict(polar=polar_options[1]))
    fig3, ax3 = plt.subplots(subplot_kw=dict(polar=polar_options[2]))
    fig4, ax4 = plt.subplots(subplot_kw=dict(polar=polar_options[3]))
    fig5, ax5 = plt.subplots(subplot_kw=dict(polar=polar_options[4]))
    logged_figures = []
    graph_images = []
    all_returned_graph_images = []
    available_axes = [ax1, ax2, ax3, ax4, ax5]
    # Turn the graph count from a string to an int
    graph_count_number = len(graph_configurations)
 
    all_returned_graph_configurations = []
 
    # For every graph that was requested to be made, make the graph
    
    for graph in range(0, graph_count_number):
        if "g_type" not in graph_configurations[graph]:
            pass
        else:
            if graph_configurations[graph]["g_type"] == "Pie Graph":
                color = "#" + graph_configurations[graph]["color"]
                print("color color", color)
                graph_configurations[graph]["settings"] = {"color": [color, "blue"]}
            graph_configurations[graph]["settings"] = {"color": "#" + graph_configurations[graph]["color"]}
            print(graph_configurations[graph])
            print(graph_configurations[graph]["color"])
            axis = available_axes.pop(0)
           
            if "x_axis_label" not in graph_configurations[graph]:
                if graph_configurations[graph]["g_type"] == "Pie Graph":
                    graph_configurations[graph].update({"x_axis_label": None})
                else:
                    graph_configurations[graph].update({"x_axis_label": graph_configurations[graph]["x_axis_name"]})
            if "y_axis_label" not in graph_configurations[graph]:
                if isinstance(graph_configurations[graph]["g_type"], list):
                    graph_configurations[graph].update({"y_axis_label": None})
                else:
                    if graph_configurations[graph]["g_type"] == "Pie Graph":
                        graph_configurations[graph].update({"y_axis_label": None})
                    else:
                        graph_configurations[graph].update({"y_axis_label": graph_configurations[graph]["y_axis_name"]})
            if "title" not in graph_configurations[graph]:
                graph_configurations[graph].update({"title": None})
            if "x_data" not in graph_configurations[graph]:
                graph_configurations[graph].update({"x_data": None})
            if "y_data" not in graph_configurations[graph]:
                graph_configurations[graph].update({"y_data": None})
            if "show_legend" not in graph_configurations[graph]:
                graph_configurations[graph].update({"show_legend": False})
            if "x_range" not in graph_configurations[graph]:
                graph_configurations[graph].update({"x_range": None})
            if "y_range" not in graph_configurations[graph]:
                graph_configurations[graph].update({"y_range": None})
            if "x_axis_label_font_name" not in graph_configurations[graph]:
                graph_configurations[graph].update({"x_axis_label_font_name": "Arial"})
            if "y_axis_label_font_name" not in graph_configurations[graph]:
                graph_configurations[graph].update({"y_axis_label_font_name": "Arial"})
            if "title_font_name" not in graph_configurations[graph]:
                graph_configurations[graph].update({"title_font_name": "Arial"})
            if "x_axis_label_font_size" not in graph_configurations[graph]:
                graph_configurations[graph].update({"x_axis_label_font_size": 10})
            if "y_axis_label_font_size" not in graph_configurations[graph]:
                graph_configurations[graph].update({"y_axis_label_font_size": 10})
            if "title_font_size" not in graph_configurations[graph]:
                graph_configurations[graph].update({"title_font_size": 10})
            if "settings" not in graph_configurations[graph]:
                if isinstance(graph_configurations[graph]["g_type"], list):
                    graph_configurations[graph].update(
                        {"settings": [{} for i in range(len(graph_configurations[graph]["g_type"]))]})
                else:
                    graph_configurations[graph].update({"settings": {}})
            
            graph_dictionary, returned_graph_configuration = create_graph(
                values_dataframe=grab_data_from_urls(urls),
                axis=axis,
                graph_id=graph + 1,
                g_type=graph_configurations[graph]["g_type"],
                x_axis_name=graph_configurations[graph]["x_axis_name"],
                y_axis_name=graph_configurations[graph]["y_axis_name"],
                settings=graph_configurations[graph]["settings"],
                x_axis_label=graph_configurations[graph]["x_axis_label"],
                y_axis_label=graph_configurations[graph]["y_axis_label"],
                title=graph_configurations[graph]["title"],
                x_data=graph_configurations[graph]["x_data"],
                y_data=graph_configurations[graph]["y_data"],
                show_legend=graph_configurations[graph]["show_legend"],
                x_range=graph_configurations[graph]["x_range"],
                y_range=graph_configurations[graph]["y_range"],
                x_axis_label_font_name=graph_configurations[graph]["x_axis_label_font_name"],
                y_axis_label_font_name=graph_configurations[graph]["y_axis_label_font_name"],
                title_font_name=graph_configurations[graph]["title_font_name"],
                x_axis_label_font_size=graph_configurations[graph]["x_axis_label_font_size"],
                y_axis_label_font_size=graph_configurations[graph]["y_axis_label_font_size"],
                title_font_size=graph_configurations[graph]["title_font_size"]
            )
            logged_figures.append(graph_dictionary)
            all_returned_graph_configurations.append(returned_graph_configuration)
            graph += 1
 
    save_all_figures("svg", logged_figures)
 
    return all_returned_graph_configurations
 
 
def display_created_figures():
    plt.show()  # displaying graphs for testing purposes only
 
 

