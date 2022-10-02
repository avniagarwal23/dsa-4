class Prim:
    def __init__(self, graph):
        self.graph = graph
        self.visited = [False] * len(graph)
        self.mst = []
        self.prim()

    def prim(self):
        self.visited[0] = True
        for _ in range(len(self.graph) - 1):
            min_edge = None
            for i in range(len(self.graph)):
                if self.visited[i]:
                    for j in range(len(self.graph)):
                        if not self.visited[j] and self.graph[i][j] != 0:
                            if min_edge is None:
                                min_edge = (i, j, self.graph[i][j])
                            elif self.graph[i][j] < min_edge[2]:
                                min_edge = (i, j, self.graph[i][j])
            self.mst.append(min_edge)
            self.visited[min_edge[1]] = True

    def print_mst(self):
        for edge in self.mst:
            print(str(edge[0]) + " - " + str(edge[1]) + " : " + str(edge[2]))

    def __str__(self):
        return str(self.mst)

def main():
    graph = [[0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
    prim = Prim(graph)
    prim.print_mst()

if __name__ == "__main__":
    main()
