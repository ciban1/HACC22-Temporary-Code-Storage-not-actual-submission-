from graph_functions import create_multiple_graphs, save_all_figures, display_figures, column_headers, combine_dataframes, sql_query_link_converter

# homeless_shelter_locations_link = 'https://opendata.hawaii.gov/api/3/action/datastore_search_sql?sql=SELECT%20
# *%20from%20%22158d4b5b-0b84-4f27-948e-6eb7a16131f4%22'

# ---------------------------------------------------- Create Graphs ---------------------------------------------------
# available_graph_types = ["bar", "line", "scatter", "pie", "geo"]
# available_arguments = [data_values, graph_type: str, <--- Required arguments
#                        color, title, x_axis_label, y_axis_label, horizontal_bar: bool, pie_colors]
#
# For pie charts: x is the labels of each slice while y is the sizes of each slice
url_list = ["https://opendata.hawaii.gov/dataset/ab266790-2f8f-46dd-a39e-0b340d769558/resource/2b08800c-2697-4d8b-9911-6de9d6e9cf42/download/proficiency-on-hsa-in-reading-grade-4-csv.csv"]
# combine_dataframes([sql_query_link_converter("https://opendata.hawaii.gov/dataset/ab266790-2f8f-46dd-a39e-0b340d769558/resource/2b08800c-2697-4d8b-9911-6de9d6e9cf42/download/proficiency-on-hsa-in-reading-grade-4-csv.csv")])

print(column_headers(url_list[0]))
create_multiple_graphs(
   url="https://opendata.hawaii.gov/dataset/ab266790-2f8f-46dd-a39e-0b340d769558/resource/2b08800c-2697-4d8b-9911-6de9d6e9cf42/download/proficiency-on-hsa-in-reading-grade-4-csv.csv",
   graph_count_string="2",
   graph_type_list=["line", "scatter"],
   x_axis_column_name_list=["County", "County"],
   y_axis_column_name_list=["Percent", "Percent"]
)

# ----------------------------------------------- Save and Display Graphs ----------------------------------------------

save_all_figures("svg")
display_figures()
