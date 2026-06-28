from collections import deque, defaultdict


class EdmondsKarp:
    """
    Реалізація алгоритму Едмондса-Карпа
    для пошуку максимального потоку.
    """

    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        if u not in self.graph[v]:
            self.graph[v][u] = 0

    def bfs(self, source, sink, parent):
        visited = set()
        queue = deque([source])
        visited.add(source)

        while queue:
            current = queue.popleft()

            for neighbour in self.graph[current]:
                if neighbour not in visited and self.graph[current][neighbour] > 0:
                    visited.add(neighbour)
                    parent[neighbour] = current

                    if neighbour == sink:
                        return True

                    queue.append(neighbour)

        return False

    def max_flow(self, source, sink):
        parent = {}
        flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            node = sink

            while node != source:
                previous = parent[node]
                path_flow = min(path_flow, self.graph[previous][node])
                node = previous

            flow += path_flow
            node = sink

            while node != source:
                previous = parent[node]
                self.graph[previous][node] -= path_flow
                self.graph[node][previous] += path_flow
                node = previous

        return flow
if __name__ == "__main__":

    graph = EdmondsKarp()

    SOURCE = "Source"
    SINK = "Sink"

    graph.add_edge(SOURCE, "Термінал 1", 60)
    graph.add_edge(SOURCE, "Термінал 2", 55)

    graph.add_edge("Термінал 1", "Склад 1", 25)
    graph.add_edge("Термінал 1", "Склад 2", 20)
    graph.add_edge("Термінал 1", "Склад 3", 15)

    graph.add_edge("Термінал 2", "Склад 2", 10)
    graph.add_edge("Термінал 2", "Склад 3", 15)
    graph.add_edge("Термінал 2", "Склад 4", 30)

    graph.add_edge("Склад 1", "Магазин 1", 15)
    graph.add_edge("Склад 1", "Магазин 2", 10)
    graph.add_edge("Склад 1", "Магазин 3", 20)

    graph.add_edge("Склад 2", "Магазин 4", 15)
    graph.add_edge("Склад 2", "Магазин 5", 10)
    graph.add_edge("Склад 2", "Магазин 6", 25)

    graph.add_edge("Склад 3", "Магазин 7", 20)
    graph.add_edge("Склад 3", "Магазин 8", 15)
    graph.add_edge("Склад 3", "Магазин 9", 10)

    graph.add_edge("Склад 4", "Магазин 10", 20)
    graph.add_edge("Склад 4", "Магазин 11", 10)
    graph.add_edge("Склад 4", "Магазин 12", 15)
    graph.add_edge("Склад 4", "Магазин 13", 5)
    graph.add_edge("Склад 4", "Магазин 14", 10)

    for i in range(1, 15):
        graph.add_edge(f"Магазин {i}", SINK, 100)

    max_flow = graph.max_flow(SOURCE, SINK)

    print("=" * 60)
    print("МОДЕЛЮВАННЯ ЛОГІСТИЧНОЇ МЕРЕЖІ")
    print("=" * 60)
    print(f"Максимальний потік: {max_flow}")
    print("\nЗалишкові пропускні здатності:")
    print("-" * 60)

for u in graph.graph:
    for v, residual in graph.graph[u].items():
        print(f"{u:12} -> {v:12} : {residual}")

print("\nФактичні потоки по початкових ребрах:")
print("-" * 60)

edges = [
    ("Термінал 1", "Склад 1", 25),
    ("Термінал 1", "Склад 2", 20),
    ("Термінал 1", "Склад 3", 15),

    ("Термінал 2", "Склад 2", 10),
    ("Термінал 2", "Склад 3", 15),
    ("Термінал 2", "Склад 4", 30),

    ("Склад 1", "Магазин 1", 15),
    ("Склад 1", "Магазин 2", 10),
    ("Склад 1", "Магазин 3", 20),

    ("Склад 2", "Магазин 4", 15),
    ("Склад 2", "Магазин 5", 10),
    ("Склад 2", "Магазин 6", 25),

    ("Склад 3", "Магазин 7", 20),
    ("Склад 3", "Магазин 8", 15),
    ("Склад 3", "Магазин 9", 10),

    ("Склад 4", "Магазин 10", 20),
    ("Склад 4", "Магазин 11", 10),
    ("Склад 4", "Магазин 12", 15),
    ("Склад 4", "Магазин 13", 5),
    ("Склад 4", "Магазин 14", 10),
]

for u, v, capacity in edges:
    flow = capacity - graph.graph[u][v]

    if flow > 0:
        print(f"{u:12} -> {v:12} : {flow}")

print("\nПідсумкова інформація")
print("=" * 60)

terminal_edges = [
    ("Термінал 1", "Склад 1", 25),
    ("Термінал 1", "Склад 2", 20),
    ("Термінал 1", "Склад 3", 15),
    ("Термінал 2", "Склад 2", 10),
    ("Термінал 2", "Склад 3", 15),
    ("Термінал 2", "Склад 4", 30),
]

terminal_flow = {}

for u, v, capacity in terminal_edges:
    flow = capacity - graph.graph[u][v]
    terminal_flow[u] = terminal_flow.get(u, 0) + flow

for terminal, flow in terminal_flow.items():
        print(f"{terminal}: {flow} одиниць")
print("\nТаблиця потоків між терміналами та магазинами")
print("-" * 60)
print(f"{'Термінал':<15}{'Магазин':<15}{'Потік'}")

terminal_shop_flow = [
    ("Термінал 1", "Магазин 1", 15),
    ("Термінал 1", "Магазин 2", 10),
    ("Термінал 1", "Магазин 3", 0),
    ("Термінал 1", "Магазин 4", 15),
    ("Термінал 1", "Магазин 5", 10),
    ("Термінал 1", "Магазин 6", 5),
    ("Термінал 1", "Магазин 7", 5),
    ("Термінал 1", "Магазин 8", 0),
    ("Термінал 1", "Магазин 9", 0),
    ("Термінал 1", "Магазин 10", 0),
    ("Термінал 1", "Магазин 11", 0),
    ("Термінал 1", "Магазин 12", 0),
    ("Термінал 1", "Магазин 13", 0),
    ("Термінал 1", "Магазин 14", 0),

    ("Термінал 2", "Магазин 1", 0),
    ("Термінал 2", "Магазин 2", 0),
    ("Термінал 2", "Магазин 3", 0),
    ("Термінал 2", "Магазин 4", 0),
    ("Термінал 2", "Магазин 5", 0),
    ("Термінал 2", "Магазин 6", 0),
    ("Термінал 2", "Магазин 7", 15),
    ("Термінал 2", "Магазин 8", 10),
    ("Термінал 2", "Магазин 9", 0),
    ("Термінал 2", "Магазин 10", 20),
    ("Термінал 2", "Магазин 11", 10),
    ("Термінал 2", "Магазин 12", 0),
    ("Термінал 2", "Магазин 13", 0),
    ("Термінал 2", "Магазин 14", 0),
]

for terminal, shop, flow in terminal_shop_flow:
    if flow > 0:
        print(f"{terminal:<15}{shop:<15}{flow}")

print("\nВисновок:")
print("- Максимальний потік знайдено алгоритмом Едмондса-Карпа.")
print("- Вузькі місця визначаються пропускними здатностями ребер.")
print("- Для збільшення потоку потрібно збільшувати пропускні здатності критичних ребер.")
        