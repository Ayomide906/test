"""This code will give the shortest path and all the paths"""
class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        #I need a dictionary that maps all nodes to its edges
        for idx,element in enumerate(self.edges,0):
            if element[0] in self.graph_dict.keys():
                self.graph_dict[element[0]].append(element[1])
            else:
                self.graph_dict[element[0]] = [element[1]]
        print("Graph dict: ",self.graph_dict)
    def get_paths(self,start,end,path=[]):
        if start != end:
            path = path + [start + '-->']
        if start == end:
            return [path+ [end]]
        if start not in self.graph_dict:
            return []
        paths=[]
        q=[]
        for node in self.graph_dict[start]:
            if node not in path:
                #recursively check elements of start connected to end
                new_paths=self.get_paths(node,end,path)
                for p in new_paths:
                    paths.append(p)

        return paths
    def get_shortest_path(self, starter,ender):
        path=self.get_paths(starter,ender)
        previous_length=0
        least=[]
        if path is []:
            return f"There is no path connecting {starter} and {ender}"
        for idx,element in enumerate(path):
            length=len(element)
            if length< previous_length:
                least= path[idx]
            previous_length=length
        return least



if __name__=='__main__':
    #to store the pairs of nodes we have in a graph, I stored the pairs as a tuple and put the graph system as a list
    routes=[
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]
    route_graph=Graph(routes)
    start="Mumbai"
    end="Dubai"
    print(f"path between {start} and {end}: ",route_graph.get_paths(start,end))
    starter=input("Enter the starting point: ")
    ender=input("Enter the ending point: ")
    tttty=route_graph.get_shortest_path(starter,ender)
    print(f"The shortest path from {starter} to {ender} is: ",tttty)