import pandas as pd
import networkx as nx
import math

def generate_network(file: str) -> nx.DiGraph:
    data = pd.read_csv(file)

    # Initialize an empty directed graph
    G = nx.DiGraph()

    # Iterate through each row in the dataset
    for index, row in data.iterrows():
        # Extract the origin, destination, and other relevant information
        origin = row['ORIGIN']
        destination = row['DEST']
        
        # Check if there's already an edge between the origin and destination
        if G.has_edge(origin, destination):
            # If so, increment the weight (number of flights) by 1
            G[origin][destination]['weight'] += 1
        else:
            # Otherwise, add a new edge with a weight of 1
            G.add_edge(origin, destination, weight=1)
    
    return G

def generate_network_without_edge_weight(file: str) -> nx.DiGraph:
    data = pd.read_csv(file)

    # Initialize an empty directed graph
    G = nx.DiGraph()

    # Iterate through each row in the dataset
    for index, row in data.iterrows():
        # Extract the origin, destination, and other relevant information
        origin = row['ORIGIN']
        destination = row['DEST']
        
        G.add_edge(origin, destination, weight=1)
    
    return G

def generate_network_based_on_delay(file: str, delay_column: str) -> nx.Graph:
    data = pd.read_csv(file)

    # Initialize an empty directed graph
    G = nx.Graph()

    for index, row in data.iterrows():
        # Extract the origin, destination, and other relevant information
        origin = row['ORIGIN']
        
        if not G.has_node(origin):
            G.add_node(origin, delay=0.0)

        delay_value = row[delay_column]

        if not math.isnan(delay_value):
            G.nodes[origin]['delay'] += delay_value
    
    return G