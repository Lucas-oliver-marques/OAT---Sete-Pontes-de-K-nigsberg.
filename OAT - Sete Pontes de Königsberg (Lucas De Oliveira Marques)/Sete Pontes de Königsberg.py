class Graph:
    def __init__(self, vertices):
        self.graph = {}
        self.vertices = vertices
        for vertex in vertices:
            self.graph[vertex] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_connected(self):
        visited = {vertex: False for vertex in self.vertices}
        stack = []

        for vertex in self.vertices:
            if len(self.graph[vertex]) > 0:
                start_vertex = vertex
                break

        stack.append(start_vertex)
        visited[start_vertex] = True

        while stack:
            u = stack.pop()
            for v in self.graph[u]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)

        for vertex in self.vertices:
            if not visited[vertex] and len(self.graph[vertex]) > 0:
                return False

        return True

    def is_eulerian(self):
        if not self.is_connected():
            return False

        odd_degree_vertices = 0
        for vertex in self.vertices:
            if len(self.graph[vertex]) % 2 != 0:
                odd_degree_vertices += 1

        return odd_degree_vertices == 0 or odd_degree_vertices == 2

    def find_eulerian_path(self):
        if not self.is_eulerian():
            return None

        stack = []
        path = []
        current_vertex = None

        for vertex in self.vertices:
            if len(self.graph[vertex]) % 2 != 0:
                current_vertex = vertex
                break

        if current_vertex is None:
            current_vertex = self.vertices[0]

        stack.append(current_vertex)

        while stack:
            if len(self.graph[current_vertex]) == 0:
                path.append(current_vertex)
                current_vertex = stack.pop()
            else:
                stack.append(current_vertex)
                next_vertex = self.graph[current_vertex][0]
                self.graph[current_vertex].remove(next_vertex)
                self.graph[next_vertex].remove(current_vertex)
                current_vertex = next_vertex

        path.append(current_vertex)
        return path

vertices = ['A', 'B', 'C', 'D']
edges = [('A', 'B'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]

g = Graph(vertices)
for u, v in edges:
    g.add_edge(u, v)

if g.is_eulerian():
    path = g.find_eulerian_path()
    print("Caminho Euleriano encontrado:", path)
else:
    print("Não é possível encontrar um Caminho Euleriano no grafo dado.")
