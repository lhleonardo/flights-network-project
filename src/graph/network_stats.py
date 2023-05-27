import networkx as nx
import powerlaw as pw

def nodes_count(G: nx.DiGraph) -> int:
    return G.number_of_nodes()

def average_degree(G: nx.DiGraph) -> float:
    N = nodes_count(G)
    total_degrees = sum([G.in_degree(node) + G.out_degree(node) for node in G.nodes()])
    return total_degrees / N

def average_squared_degree(G: nx.DiGraph) -> tuple[float, float]:
    N = nodes_count(G)
    average_squared_in_degree = sum([G.in_degree(node) ** 2 for node in G.nodes()]) / N
    average_squared_out_degree = sum([G.out_degree(node) ** 2 for node in G.nodes()]) / N

    return (average_squared_in_degree, average_squared_out_degree)

def gamma_values(G: nx.DiGraph) -> tuple[float, float]:
    # Get the in-degree and out-degree lists
    in_degrees = [G.in_degree(node) for node in G.nodes()]
    out_degrees = [G.out_degree(node) for node in G.nodes()]

    # Fit a power-law distribution to the in-degree and out-degree data
    in_degree_fit = pw.Fit(in_degrees, discrete=True)
    out_degree_fit = pw.Fit(out_degrees, discrete=True)

    # Get the in-degree and out-degree exponents (γin and γout)
    gamma_in = in_degree_fit.alpha
    gamma_out = out_degree_fit.alpha