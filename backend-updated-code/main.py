from graph_functions import create_multiple_graphs, display_figures

create_multiple_graphs(
    url=["https://opendata.hawaii.gov/dataset/0ed29f84-3ebe-4484-b2bd-916ed6f0410b/resource/032f5da0-7ea1-41b6-a27d-03abefba12af/download/point-in-time-count-children-experiencing-homelessness-as-of-2022.csv"],
    x_axis_column_name_list=["Year", "Year"],
    y_axis_column_name_list=[["Hawaii, Maui, and Kauai", "Oahu", "Total"], "Total"],
    graph_count_string="2",
    graph_type_list=[["line", "line", "line"], "bar"]
)

display_figures()
