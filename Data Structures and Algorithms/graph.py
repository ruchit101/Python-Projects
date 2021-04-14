print("Ab toh khatam krr le bhai!!!!")


# Ruchit Bagade
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph dict:", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path+[start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def shortest_path(self,start,end ,path=[]):
        all_paths=self.get_paths(start,end)
        min=[1,2,3,4,5,6,7,8,9]
        for i in all_paths:
            if len(i) < len(min):
                min=i
        return min

if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    Route_graph = Graph(routes)
    start = "Dubai"
    end = "New York"
    print(f"Paths Between {start} and {end}:",Route_graph.get_paths(start,end))
    print(f"Paths Between {start} and {end}:", Route_graph.shortest_path(start, end))