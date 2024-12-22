class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, source, destination, weight):
        self.edges.append(Edge(source, destination, weight))

    def find_parent(self, parent, vertex):
        if parent[vertex] != vertex:
            parent[vertex] = self.find_parent(parent, parent[vertex])  # Path compression
        return parent[vertex]

    def union(self, parent, rank, root1, root2):
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root2] > rank[root1]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

    def kruskal_mst(self):
        # Step 1: Sort edges by weight
        self.edges.sort()

        # Initialize parent and rank arrays
        parent = [i for i in range(self.vertices)]
        rank = [0] * self.vertices

        mst = []  # List to store the MST edges
        mst_cost = 0

        # Process edges one by one
        for edge in self.edges:
            root1 = self.find_parent(parent, edge.source)
            root2 = self.find_parent(parent, edge.destination)

            if root1 != root2:  # No cycle
                mst.append(edge)
                mst_cost += edge.weight
                self.union(parent, rank, root1, root2)

        # Print the MST and its total cost
        print("Edges in MST:")
        for edge in mst:
            print(f"{edge.source} -- {edge.destination} == {edge.weight}")
        print(f"Total cost of MST: {mst_cost}")


# Example usage:
if __name__ == "__main__":
    graph = Graph(4)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 6)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 4)

    graph.kruskal_mst()
