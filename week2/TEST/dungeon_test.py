import unittest
from dungeon import Dungeon
import os


#Test

class test_smtg_test(unittest.TestCase):
    """Testing the unit"""

    def setUp(self):
        self.filename = 'test_dng_map.txt'
        f = open(self.filename, "w")
        content_map = 'S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S'
        f.write(content_map)
        f.close()

        self.new_map = Dungeon(self.filename)

    def test_load_map(self):
        expected = 'S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S'
        self.assertEqual(expected, self.new_map.load_map())

    def test_map_to_matrix(self):
        expected = [['S', '.', '#', '#', '.', '.', '.', '.', '.', '.'], ['#', '.', '#', '#', '.', '.', '#', '#', '#', '.'], ['#', '.', '#', '#', '#', '.', '#', '#', '#', '.'], ['#', '.', '.', '.', '.', '.', '#', '#', '#', '.'], ['#', '#', '#', '.', '#', '#', '#', '#', '#', 'S']]

        self.assertEqual(expected, self.new_map.map_to_matrix())

    def tearDown(self):
        # fpath = os.getcwd()
        try:
            os.remove(self.filename)
        except OSError:
            print('No such file')


if __name__ == '__main__':
    unittest.main()
