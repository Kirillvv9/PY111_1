from typing import Hashable, List
import networkx as nx


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    path_node = []
    wait_node = []
    visited_node = {node: False for node in g.nodes}
    wait_node.append(start_node)
    visited_node[start_node] = True

    while wait_node:
        current_node = wait_node.pop()
        neighbours = g[current_node]
        for neighbor in neighbours:
            if not visited_node[neighbor]:
                wait_node.append(neighbor)
                visited_node[neighbor] = True
        path_node.append(current_node)

    return path_node
