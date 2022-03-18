from typing import Hashable, List
from collections import deque

import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    visited_nodes = {node: False for node in g.nodes}  # то, что посетили
    path_nodes = []  # сгоревшие узлы

    wait_nodes = deque()  # очередь из узлов, ожидающих обхода
    wait_nodes.append(start_node)  # подожгли первый узел
    visited_nodes[start_node] = True  # добавили узел в очередь - он посещенный

    while wait_nodes:  # пока очередь не пуста
        current_node = wait_nodes.popleft()  # берем горящий узел из начала очереди
        path_nodes.append(current_node)  #

        for neighbour in g[current_node]:
            if not visited_nodes[neighbour]:
                wait_nodes.append(neighbour)  # подожгли соседа
                visited_nodes[neighbour] = True

    return path_nodes

