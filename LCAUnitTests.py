import unittest
import LCAImplementation


class Node(LCAImplementation.Node):
    def __init__(self, value):
        super().__init__(value)


class TestLCA(unittest.TestCase):

    def test_BasicTree(self):
        #print("Test1: Test Basic Tree:")
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        # visualising the data

        #print(root)

        self.assertEqual(3, LCAImplementation.findLCA(root, 6, 7), "3 should be the lowest common ancestor of 6 and 7")

    def test_EmptyTree(self):
        #print("Test2: Test Empty Tree:")
        root = None
        self.assertEqual(-1, LCAImplementation.findLCA(root, 6, 7), " The output should be -1 since the tree is empty")

    def test_BothNodesNotPresent(self):
        #print("Test3: testBothNodesNotPresent:")
        root = Node(1)
        self.assertEqual(-1, LCAImplementation.findLCA(root, 6, 7), " The output should be -1 both nodes are missing")

    def test_OneNodeNotPresent(self):
        #print("Test4: testOneNodeNotPresent:")
        root = Node(1)
        root.left = Node(6)
        self.assertEqual(-1, LCAImplementation.findLCA(root, 6, 7), " The output should -1 since one of the nodes is missing")

    def test_CommonAncestorIsTarg(self):
        #print("Test5: commonAncestorIsTarget")
        root = Node(1)
        root.left = Node(3)
        root.right = Node(5)
        root.left.left = Node(6)
        root.left.right = Node(8)

        self.assertEqual(1, LCAImplementation.findLCA(root, 1, 3),
                         "The output should be 1 since it is both the ancestor node and the target node")
        self.assertEqual(1, LCAImplementation.findLCA(root, 1, 5),
                         "The output should be 1 since it is both the ancestor node and the target node")
        self.assertEqual(3, LCAImplementation.findLCA(root, 3, 6),
                         "The output should be 3 since it is both the ancestor node and the target node")
        self.assertEqual(3, LCAImplementation.findLCA(root, 3, 8),
                         "The output should be 3 since it is both the ancestor node and the target node")


    def test_MissingNode(self):
        #print("Test6: testMissingNode")
        root = Node(1)
        root.left = Node(2)
        root.right = Node(31)
        root.left.left = Node(4)
        root.left.right = Node(10)
        root.right.left = Node(16)
        root.right.right = Node(7)
        root.left.left.left = Node(24)
        self.assertEqual(-1, LCAImplementation.findLCA(root, 10, 9), "Missing node should return -1")

    def test_DuplicateNodesLucky(self):
        #print("Test7: duplicateNodesLucky")
        root = Node(1)
        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(4)
        root.left.right = Node(10)
        root.right.left = Node(50)
        root.right.right = Node(7)
        root.left.left.left = Node(24)
        self.assertEqual(1, LCAImplementation.findLCA(root, 1, 2), "Both the common ancestor and target are separate nodes both"\
                                                           "storing the value 1")

    def test_DuplicateNodes(self):
        # print("Test8: duplicateNodes:")
        root = Node(1)
        root.left = Node(3)
        root.right = Node(2)
        root.left.left = Node(4)
        root.left.right = Node(6)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(24)
        self.assertEqual(1, LCAImplementation.findLCA(root, 7, 6),
                         "There are two instances of the value 6 in the tree, 1 should be returned as it is the common"
                         "ancestor for both values of 6")

        #Example of visualization
        print("Test 8: test_DuplicateNodes")
        print(root)

    def test_Single(self):
        # print("Test9: testSingle")
        root = Node(1)

        assert LCAImplementation.findLCA(root, 1, 1) == 1, \
            "Should be 1 but got: " + str(LCAImplementation.findLCA(root, 1, 1))

    def test_CharsInNumberTree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(31)
        root.left.left = Node(4)
        root.left.right = Node(10)
        root.right.left = Node(16)
        root.right.right = Node(7)
        root.left.left.left = Node(24)

        self.assertEqual(-1, LCAImplementation.findLCA(root, 'a', 'b'),
                         "Should be -1 but got: " + str(LCAImplementation.findLCA(root, 'a', 'b')))

    def test_CharsInCharTree(self):
        root = Node('a')
        root.left = Node('b')
        root.right = Node('c')
        root.left.left = Node('d')
        root.left.right = Node('e')
        root.right.left = Node('f')
        root.right.right = Node('g')
        root.left.left.left = Node('h')

        self.assertEqual('b', LCAImplementation.findLCA(root, 'd', 'e'),
                         "Should be b but got: " + str(LCAImplementation.findLCA(root, 'd', 'e')))

    def test_DAG(self):
        root=Node('a')
        root.further.left = Node('b')
        root.right = Node('c')
        root.left = root.right.left =Node('d')
        root.further.right = root.right.right = root.left.right = Node('e')
        # Used further to avoid deleting nodes when nodes have more than one parent or more than two children.
        # The code doesn't work. This proves we need a new implementation for a DAG.

    





if __name__ == '__main__':
    unittest.main()
