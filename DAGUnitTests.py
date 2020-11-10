import DAG
import unittest


class test_Dag_LCA(unittest.TestCase):

    def test_DAGvertices(self):
        correct = ['A', 'B', 'C', 'D']
        testDag = DAG.DAG()
        testDag.add_vertex("A")
        testDag.add_vertex("B")
        testDag.add_vertex("C")
        testDag.add_vertex("D")

        self.assertEqual(correct, testDag.vertices(), "Incorrect result:" + str(testDag.vertices()))

    def test_DAGedges(self):
        correct = [['A', 'B'], ['B', 'C'], ['C', 'D']]
        testDag = DAG.DAG()
        testDag.add_vertex("A")
        testDag.add_vertex("B")
        testDag.add_vertex("C")
        testDag.add_vertex("D")

        testDag.add_edge (["A","B"])
        testDag.add_edge(["B","C"])
        testDag.add_edge(["C","D"])



        self.assertEqual(correct, testDag.edges(), "Incorrect result:" + str(testDag.edges()))

    def test_basicDAGPrinting(self):
        correct = {'A': ['B'], 'B': ['C'], 'C': ['D'], 'D': []}
        testDag = DAG.DAG()
        testDag.add_vertex("A")
        testDag.add_vertex("B")
        testDag.add_vertex("C")
        testDag.add_vertex("D")

        testDag.add_edge(["A", "B"])
        testDag.add_edge(["B", "C"])
        testDag.add_edge(["C", "D"])

        dictionary = testDag.graphDict()
        self.assertEqual(correct, dictionary, "Incorrect result:" + str(dictionary))

    def test_lineDAG_LCA(self):

        testDag = DAG.DAG()
        testDag.add_vertex("A")
        testDag.add_vertex("B")
        testDag.add_vertex("C")
        testDag.add_vertex("D")

        testDag.add_edge(["A", "B"])
        testDag.add_edge(["B", "C"])
        testDag.add_edge(["C", "D"])

        self.assertEqual(['B'], DAG.DAG_LCA.findLCA(testDag, "B", "C"), "Incorrect result:" + str(DAG.DAG_LCA.findLCA(testDag, "B", "C")))

    def test_exampleDAG_LCA_simple(self):
        testDag = DAG.DAG()

        testDag.add_vertex("G")
        testDag.add_vertex("F")
        testDag.add_vertex("E")
        testDag.add_vertex("D")
        testDag.add_vertex("C")
        testDag.add_vertex("B")
        testDag.add_vertex("A")

        testDag.add_edge(["G", "F"])
        testDag.add_edge(["G", "D"])
        testDag.add_edge(["F", "E"])
        testDag.add_edge(["D", "C"])
        testDag.add_edge(["C", "B"])
        testDag.add_edge(["E", "B"])
        testDag.add_edge(["B", "A"])

        self.assertEqual(['G'], DAG.DAG_LCA.findLCA(testDag, "C", "E"),
                         "Incorrect result:" + str(DAG.DAG_LCA.findLCA(testDag, "C", "E")))

    def test_exampleDAG_LCA_duplicate_Target(self):
        testDag = DAG.DAG()

        testDag.add_vertex("G")
        testDag.add_vertex("F")
        testDag.add_vertex("E")
        testDag.add_vertex("D")
        testDag.add_vertex("C")
        testDag.add_vertex("B")
        testDag.add_vertex("A")

        testDag.add_edge(["G", "F"])
        testDag.add_edge(["G", "D"])
        testDag.add_edge(["F", "E"])
        testDag.add_edge(["D", "C"])
        testDag.add_edge(["C", "B"])
        testDag.add_edge(["E", "B"])
        testDag.add_edge(["B", "A"])

        self.assertEqual(['G'], DAG.DAG_LCA.findLCA(testDag, "G", "G"),
                         "Incorrect result:" + str(DAG.DAG_LCA.findLCA(testDag, "G", "G")))


    def test_MissingNode(self):
        testDag = DAG.DAG()

        testDag.add_vertex("G")
        testDag.add_vertex("F")
        testDag.add_vertex("E")
        testDag.add_vertex("D")
        testDag.add_vertex("C")
        testDag.add_vertex("B")
        testDag.add_vertex("A")

        testDag.add_edge(["G", "F"])
        testDag.add_edge(["G", "D"])
        testDag.add_edge(["F", "E"])
        testDag.add_edge(["D", "C"])
        testDag.add_edge(["C", "B"])
        testDag.add_edge(["E", "B"])
        testDag.add_edge(["B", "A"])

        self.assertEqual(None, DAG.DAG_LCA.findLCA(testDag, "Z", "E"),
                         "Incorrect result:" + str(DAG.DAG_LCA.findLCA(testDag, "Z", "E")))

    def test_TwoMissingNodes(self):
        testDag = DAG.DAG()

        testDag.add_vertex("G")
        testDag.add_vertex("F")
        testDag.add_vertex("E")
        testDag.add_vertex("D")
        testDag.add_vertex("C")
        testDag.add_vertex("B")
        testDag.add_vertex("A")

        testDag.add_edge(["G", "F"])
        testDag.add_edge(["G", "D"])
        testDag.add_edge(["F", "E"])
        testDag.add_edge(["D", "C"])
        testDag.add_edge(["C", "B"])
        testDag.add_edge(["E", "B"])
        testDag.add_edge(["B", "A"])

        self.assertEqual(None, DAG.DAG_LCA.findLCA(testDag, "Z", "Y"),
                         "Incorrect result:" + str(DAG.DAG_LCA.findLCA(testDag, "Z", "Y")))

    def test_Single(self):

        testDag = DAG.DAG()
        testDag.add_vertex("G")

        self.assertEqual(['G'], DAG.DAG_LCA.findLCA(testDag, "G", "G"),
                         "Incorrect result:" + str(DAG.DAG_LCA.findLCA(testDag, "G", "G")))

    def test_EmpytyTree(self):
        testDag = DAG.DAG()

        self.assertEqual( None, DAG.DAG_LCA.findLCA(testDag, "G", "G"),
                         "Incorrect result:" + str(DAG.DAG_LCA.findLCA(testDag, "G", "G")))

    def test_unusualIntInput(self):
        testDag = DAG.DAG()

        self.assertEqual(None, DAG.DAG_LCA.findLCA(testDag, 1, 1),
                         "Incorrect result:" + str(DAG.DAG_LCA.findLCA(testDag, 1, 1)))




if __name__ == '__main__':
    unittest.main()