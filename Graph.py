"""
A graph is a pictorial representation of a set of objects where some pairs of objects are connected by links.
The interconnected objects are represented by points termed as vertices, and the links that connect the vertices are called edges.

Example:

a---c---d
|   |   |
b   e---f

The graph above is:
V= {a,b,c,d,e,f}
E= {ac,ab,cd,ce,ef,df} 
"""

"""
#Example Simple Program we can use dictionary
#model graph:
#V = {a, b, c, d, e}
#E = {ab, ac, bd, cd, de}
graph = { "a" : ["b","c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ["e"],
          "e" : ["d"]
         }
	 
print(graph)
#output: {'c': ['a', 'd'], 'a': ['b', 'c'], 'e': ['d'], 'd': ['e'], 'b': ['a', 'd']}
"""

#Graph program(Using OOP-Oriented object programming)
import os

#create graph class(object)
class graph:
    #constructor for graph
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

	# Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys()) #give list of vertex

    # Get the value of edges
    def edges(self):
        return self.findedges() #give list of edges

	# Add the vertex as a key
    def addVertex(self, vrtx):
       if vrtx not in self.gdict: #if vortex not in object list then
            self.gdict[vrtx] = [] #give value of this object

    # add edge to the graph
    def AddEdge(self, edge):
        edge = set(edge) #set value edge
        (vrtx1, vrtx2) = tuple(edge) #create tuple for edge
        if vrtx1 in self.gdict: #if vortex 1 in list then
            self.gdict[vrtx1].append(vrtx2) #add vortex 2 to list
        else: #if false then
            self.gdict[vrtx1] = [vrtx2] #vortex 1 in list is vortex 2

	# List the edge names
    def findedges(self):
        edgename = [] #create list edges name
        for vrtx in self.gdict: #for vortex in list
            for nxtvrtx in self.gdict[vrtx]: # for next vortex in list
                if {nxtvrtx, vrtx} not in edgename: #if edges not in edges
                    edgename.append({vrtx, nxtvrtx}) #add edges to edgename
        return edgename #give edgename

graph_elements={} #create some library for graph
new_graph=graph(graph_elements) #create new object

while True: #while true then
    os.system("cls") #clear cmd screen
    print("=-=-= Graph Program =-=-=")
    print("=========================")
    print("vertex:",new_graph.getVertices()) #print each vertices
    print("edges:",new_graph.edges()) #print each edges
    print("=========================")
    print("1. add vertex")
    print("2. add edges")
    print("3. Exit")
    choice=int(input("Your choice[1-3]: "))
    if choice==1: #if choice 1 true then
        x=(input("Vertex value: ")) #input x value by user
        new_graph.addVertex(x) #object graph add vertex by x value
        print("Vertex add to graph")
        input("press enter to continue...")
    elif choice==2: #if choice 2 true then
        y_edges_from=(input("left vertex value: ")) #input y_edges_from value by user
        y_edges_to=(input("Right vertex value: ")) #input y_edges_to value by user
        new_graph.addVertex(y_edges_from) #object graph add vertex by y_edges_from value
        new_graph.addVertex(y_edges_to) #object graph add vertex by y_edges_to value
        new_graph.AddEdge({y_edges_from,y_edges_to}) #object graph add edge by y_edges_from and y_edges_to value
        print("Vertex & edges add to graph")
        input("press enter to continue...")
    elif choice==3: #if choice 3 true then
        os.system("cls")
        break
    else: #if choice false then
        print("Wrong input")
        input("press enter to continue...")
        os.system("cls") #clear cmd screen