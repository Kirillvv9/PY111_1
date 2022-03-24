class Graph:
    def __init__(self, G):
        self.G = G  # количество вершин
        self.start = [[] for i in range(self.G)]

    def add(self, v, w):
        """
        Создаем граф
        """
        self.start[v].append(w)
        self.start[w].append(v)

    def dfs(self, v, visited):
        """
        Обходим граф
        """
        visited[v] = True
        for i in self.start[v]:
            if not visited[i]:
                self.dfs(i, visited)

    def comp(self):
        """
        Считаем компоненты связности (несвязанные графы)
        """
        visited = [False] * self.G  # все вершины непосещенные
        count = 0  # число компонент связности

        for v in range(self.G):
            if not visited[v]:
                self.dfs(v, visited)
                count += 1

        return count


if __name__ == '__main__':
    g = Graph(7)
    g.add(0, 1)
    g.add(1, 2)
    g.add(3, 4)
    # Граф: 0-1-2, 3-4, 5, 6
    print(g.comp())
    # Ответ: 4