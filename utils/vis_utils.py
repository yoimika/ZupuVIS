import networkx as nx
from pyvis.network import Network
from configs.config import vis_config
from graph.graph import Graph, Node


def get_nodes_from_graph(graph: Graph)->tuple[list[str], list[str]]:
    """ Get all nodes from graph. 
    The nodes is used for construct pyvis Network later
    version: 0.1
    """
    ids, labels = [], []
    for node in graph.nodes:
        ids.append(node.person.get_name_with_id())
        labels.append(node.person.get_name())
    return ids, labels

def get_edges_from_graph(graph: Graph)->list[tuple[str, str]]:
    """ Get all edges from graph. include potential edges
    The edges are used for construct pyvis Network later
    version: 0.1
    """
    edges = []
    for curr_node, nei_nodes in graph.bfs(include_potential=True):
        for nei_node in nei_nodes:
            edge = (curr_node.person.get_name_with_id(), nei_node.person.get_name_with_id())
            edges.append(edge)
    return edges

