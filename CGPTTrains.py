import heapq


class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, origin, destination, weight):
        if origin not in self.edges:
            self.edges[origin] = {}
        self.edges[origin][destination] = weight

        # Since it's an undirected graph, add the reverse edge as well
        if destination not in self.edges:
            self.edges[destination] = {}
        self.edges[destination][origin] = weight

    def dijkstra(self, start, end):
        distances = {node: float('inf') for node in self.edges}
        predecessors = {node: None for node in self.edges}
        distances[start] = 0
        heap = [(0, start)]
        current_node = start
        while end != current_node:
            if not len(heap):
                return None, None
            current_distance, current_node = heapq.heappop(heap)
            if current_distance > distances[current_node]:
                continue
            if current_node in self.edges.keys():
                for neighbor, weight in self.edges[current_node].items():
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        predecessors[neighbor] = current_node
                        heapq.heappush(heap, (distance, neighbor))
        return distances, predecessors


# Create a graph
graph = Graph()

# Add edges
edges = {
    "Amsterdam": {"Den Haag": 46, "Den Helder": 77, "Utrecht": 26},
    "Den Haag": {"Amsterdam": 46, "Eindhoven": 89},
    "Den Helder": {"Amsterdam": 77},
    "Utrecht": {"Amsterdam": 26, "Eindhoven": 47, "Zwolle": 51},
    "Eindhoven": {"Den Haag": 89, "Utrecht": 47, "Maastricht": 63, "Nijmegen": 55},
    "Maastricht": {"Eindhoven": 63, "Nijmegen": 111},
    "Nijmegen": {"Eindhoven": 55, "Maastricht": 111, "Zwolle": 77},
    "Zwolle": {"Utrecht": 51, "Nijmegen": 77},
    "Enschede": {"Zwolle": 50},
    "Groningen": {"Leeuwarden": 34, "Meppel": 49},
    "Leeuwarden": {"Groningen": 34, "Meppel": 40},
    "Meppel": {"Groningen": 49, "Leeuwarden": 40}
}
input_lst = []
lineinput = input()
while lineinput != "!":
    input_lst.append(lineinput)
    lineinput = input()

# Test Dijkstra's algorithm
line = 0
number = int(input_lst[0])
for n in range(number):
    line += 1
    city1 = input_lst[line]
    line += 1
    city2 = input_lst[line]
    if city2 in edges[city1]:
        del edges[city1][city2]
    if city1 in edges[city2]:
        del edges[city2][city1]

for origin, destinations in edges.items():
    for destination, weight in destinations.items():
        graph.add_edge(origin, destination, weight)

while line < len(input_lst):
    line += 1
    start_node = input_lst[line]
    line += 1
    end_node = input_lst[line]
    path = []
    distances, predecessors = graph.dijkstra(start_node, end_node)
    if distances is None:
        print("UNREACHABLE")
    else:
        final_distance = distances[end_node]
        while end_node != start_node:
            path.append(end_node)
            end_node = predecessors[end_node]
        path.append(start_node)
        path.reverse()
        for i in path:
            print(i)
        print(final_distance)
