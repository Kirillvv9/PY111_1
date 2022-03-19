def dfs(g, s, S = set()):
    P, Q = dict(), set()
    P[s] = None  # узел первый по счету
    Q.add(s)  # начнем поиск с s
    while Q:
        u = Q.pop()
        for v in g[u].difference(P, S):  # получим новый узел
            Q.add(v)
            P[v] = u  # записываем предыдущий узел
    return P


def components(g):  # определим число компонент
    comp_svaz = []
    seen = set()
    for i in range(9):
        if i in seen:
            continue
        C = dfs(g, i)
        seen.update(C)
        comp_svaz.append(C)
    return len(comp_svaz)


if __name__ == "__main__":
    a, b, c, d, e, f, g, h, i = range(9)
    N = [
        {b, c, d, e},   # a
        {a, d},      # b
        {a, d},       # c
        {a, c, d},     # d
        {a, g, f},       # e
        {e, g},       # f
        {e, f},       # g
        {h},         # h
        {i}          # i
    ]
    comp = components(N)
    print(comp)  # равно 3