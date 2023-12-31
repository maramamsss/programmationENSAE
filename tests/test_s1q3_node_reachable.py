# This will work if ran from the root folder.
import sys
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_Reachability(unittest.TestCase):
    def test_network00(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(g.get_path_with_power(1, 4, 11)[1], [1, 2, 3, 4])
        self.assertEqual(g.get_path_with_power(1, 4, 10)[1], None)

    def test_network02(self):
        g = graph_from_file("input/network.02.in")
        self.assertIn(g.get_path_with_power(1, 2, 11)[1], [[1, 2], [1, 4, 3, 2]])
        self.assertEqual(g.get_path_with_power(1, 2, 5)[1], [1, 4, 3, 2])

    def test_network04(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.get_path_with_power(1,2,1)[1],None)


if __name__ == '__main__':
    unittest.main()
