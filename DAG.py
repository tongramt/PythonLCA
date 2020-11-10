
# Found on Github by searching LCA DAG and Python

import itertools

class DAG_LCA:

    def findLCA(dag, v1, v2):

        # Checks for missing nodes
        Nodes = set(dag.vertices())
        if (v2 not in Nodes or v1 not in Nodes):
            # print("Chosen Nodes are not present")
            return None

        dagDict = dag.graphDict()
        dagDict
        solution = []

        anc1 = [v1]
        anc2 = [v2]
        v1ancestors = DAG_LCA.getAncestors(v1, dagDict, anc1)
        v2ancestors = DAG_LCA.getAncestors(v2, dagDict, anc2)

        if v1ancestors == []:
            v1ancestors = [v1]
        if v2ancestors == []:
            v2ancestors = [v1]

        for i in v1ancestors:
            for j in v2ancestors:
                if i == j:
                    solution.append(i)

        r = []
        # Checks for missing nodes

        for i in solution:
            dec = DAG_LCA.getDescendants(i, dagDict, [])
            for j in dec:
                for k in solution:
                    if j == k:
                        if i in solution:
                            r.append(i)

        for i in list(set(r)):
            solution.remove(i)

        return solution

    def getAncestors(v, dagDict, anc):

        if DAG_LCA.prev(v, dagDict) == []:
            return []

        anc.append(DAG_LCA.prev(v, dagDict))



        for i in DAG_LCA.prev(v, dagDict):
            anc.append(DAG_LCA.getAncestors(i, dagDict, anc))

            anc = list(itertools.chain(*anc))

        return list(set(anc))

    def prev(v, dagDict):

        prev = []

        for i in dagDict.keys():
            if v in dagDict[i]:
                prev.append(i)

        return prev

    def getDescendants(v, dagDict, dec):

        if dagDict[v] == []:
            return []

        dec.append(dagDict[v])
        dec = list(itertools.chain(*dec))

        for i in dagDict[v]:
            dec.append(DAG_LCA.getDescendants(i, dagDict, dec))
            dec = list(itertools.chain(*dec))

        return list(set(dec))

    # class to hold DAG objet


# Adopted and modified from https://www.nco.ncep.noaa.gov/pmb/codes/nwprod/nwm.v2.0.0/ush/resume_forecast/Graph.py

class DAG:

    def __init__(self, graph_dict=None):
        # initializes a graph object
        # If no dictionary or None is given, an empty dictionary will be used

        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        # returns the vertices of a DAG
        return list(self.__graph_dict.keys())

    def edges(self):
        # returns the edges of a graph
        return self.__generate_edges()

    def add_vertex(self, vertex):
        # If the vertex "vertex" is not in
        # self.__graph_dict, a key "vertex" with an empty
        # list as a value is added to the dictionary.
        # Otherwise nothing has to be done.

        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        # assumes that edge is of type set, tuple or list;
        # between two vertices can be multiple edges!
        # Adds path from first given vertex to second given vertex

        if len(edge) != 2:
            return

        vertex1, vertex2 = edge

        if vertex1 in self.__graph_dict and vertex2 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.add_vertex(vertex2)
            self.add_vertex(vertex1)
            self.__graph_dict[vertex1].append(vertex2)

    def __generate_edges(self):
        # A static method generating the edges of the
        # graph "graph". Edges are represented as sets
        # with one (a loop back to the vertex) or two
        # vertices
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                s = [vertex, neighbour]
                if s not in edges:
                    edges.append(s)
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + ", "
        res += "edges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def graphDict(self):
        return (self.__graph_dict)

# Manual Testing is commented out as unit testing provides coverage
# testDag = DAG()
# testDag.add_vertex("A")
# testDag.add_vertex("B")
# testDag.add_vertex("C")
# testDag.add_vertex("D")
#
#
# testDag.add_edge (["A","B"])
# testDag.add_edge(["B","C"])
# testDag.add_edge(["C","D"])
#
# print(testDag.edges())
# dictionary = testDag.graphDict()
# print(dictionary)


