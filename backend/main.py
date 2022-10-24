from graph_functions import import_data_values, create_graph, save_all_figures, display_figures

# ---------------------------------------------------- Import Data -----------------------------------------------------


homeless_shelter_locations = import_data_values(
   url='https://opendata.hawaii.gov/api/3/action/datastore_search_sql?sql=SELECT%20*%20from%20%22158d4b5b-0b84-4f27'
       '-948e-6eb7a16131f4%22',
   columns_to_pull=["longitude", "latitude"]
)

homeless_children = import_data_values(
   url='https://opendata.hawaii.gov/api/3/action/datastore_search_sql?sql=SELECT%20*%20from%20%22032f5da0-7ea1-41b6'
       '-a27d-03abefba12af%22',
   columns_to_pull=["Year", "Total"]
)

# ---------------------------------------------------- Create Graphs ---------------------------------------------------
# available_graph_types = ["bar", "line", "scatter", "pie", "geo"]
# available_arguments = [data_values, graph_type: str, <--- Required arguments
#                        color, title, x_axis_label, y_axis_label, horizontal_bar: bool, pie_colors]
#
# For pie charts: x is the labels of each slice while y is the sizes of each slice

create_graph(
   graph_type="geo",
   x_values=homeless_shelter_locations['longitude'],
   y_values=homeless_shelter_locations['latitude'],
   color="red",
   title="Homeless Shelters in Hawaii"
)

create_graph(
   graph_type="line",
   x_values=homeless_children["Year"],
   y_values=homeless_children["Total"],
   title="Homeless Children in Hawaii Over Time",
   x_axis_label="Year",
   y_axis_label="Total"
)

# ----------------------------------------------- Save and Display Graphs ----------------------------------------------

save_all_figures("png")
display_figures()
