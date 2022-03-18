from typing import Hashable, Mapping, Union
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    visited = {node: False for node in g.nodes}
    total_cost = {node: float("inf") for node in g.nodes}
    current_node = starting_node
    total_cost[current_node] = 0

    while True:
        visited[current_node] = True
        for neighbour_node in g[current_node]:
            edge = g[current_node][neighbour_node]
            weight = edge['weight']
            total_cost[neighbour_node] = min(total_cost[neighbour_node], total_cost[current_node] + weight)

        not_visited_total_cost = {node: cost for node, cost in total_cost.items() if not visited[node]}
        if not not_visited_total_cost:
            break
        current_node, cost = min(not_visited_total_cost.items(), key=lambda item: item[1])

    return total_cost
