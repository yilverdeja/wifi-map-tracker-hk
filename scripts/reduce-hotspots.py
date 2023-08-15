import csv
from math import radians, sin, cos, sqrt, atan2
import networkx as nx

# Calculate haversine distance between two points
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance * 1000  # Convert to meters

# Read hotspot information from CSV and create a graph
def create_graph_from_csv(filename):
    G = nx.Graph()

    with open(filename, 'r', encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        hotspots = list(reader)

    # Add nodes for each hotspot
    for hotspot in hotspots:
        attributes = {
            "SSID": hotspot["SSID"],
            "Latitude": hotspot["Latitude"],
            "Longitude": hotspot["Longitude"],
        }
        G.add_node(hotspot['LocationID'], **attributes)

    # Add edges between nodes with the same WiFi hotspot name and within 300m
    for i, hotspot1 in enumerate(hotspots):
        for hotspot2 in hotspots[i+1:]:
            if hotspot1["SSID"] == hotspot2["SSID"] and haversine_distance(float(hotspot1["Latitude"]), float(hotspot1["Longitude"]), float(hotspot2["Latitude"]), float(hotspot2["Longitude"])) < 300:
                G.add_edge(hotspot1["LocationID"], hotspot2["LocationID"])

    return G

# Function to remove nodes with 1 or more edges
def remove_nodes_with_edges(graph):
    sorted_nodes = sorted(graph.nodes(), key=lambda node: graph.degree(node), reverse=True)
    
    for node in sorted_nodes:
        if graph.degree(node) >= 1:
            graph.remove_node(node)

def recreate_csv(graph, original_filename, new_filename):
    available_nodes = list(graph.nodes())

    # Open input CSV for reading and output CSV for writing
    with open(original_filename, 'r', newline='', encoding="utf-8-sig") as input_csvfile, open(new_filename, 'w', newline='', encoding="utf-8-sig") as output_csvfile:
        reader = csv.DictReader(input_csvfile)
        fieldnames = reader.fieldnames

        # Write header to the output CSV file
        writer = csv.DictWriter(output_csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate through rows in the input CSV and write matching rows to the output CSV

        for row in reader:
            if row['LocationID'] in available_nodes:
                writer.writerow(row)

# Replace 'hotspots.csv' with your CSV file name
original_filename = 'C:/Users/yilve/Documents/Personal Projects/wifi-map-tracker-hk/wifi-map-hk.csv'
new_filename = 'C:/Users/yilve/Documents/Personal Projects/wifi-map-tracker-hk/wifi-map-hk-updated.csv'

graph = create_graph_from_csv(original_filename)

# Print the edges of the original graph
print("Original Graph Nodes:")
print(len(graph.nodes()))

# Remove nodes with 1 or more edges
remove_nodes_with_edges(graph)

# Print the edges of the updated graph
print("\nUpdated Graph Nodes:")
print(len(graph.nodes()))

# Recreate CSV based on available nodes
recreate_csv(graph, original_filename, new_filename)
print(f"\nCSV file '{new_filename}' has been created based on available nodes.")