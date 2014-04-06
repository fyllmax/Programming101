# Imports
import unittest
from solution import reduce_file_path


# Test

class test_smtg_test(unittest.TestCase):

    """Testing the unit"""

    def test_reduce_file_path(self):

        self.assertEqual("/", reduce_file_path("/"))
        # "/"
        self.assertEqual("/", reduce_file_path("/srv/../"))
        # "/"
        self.assertEqual("/srv/www/htdocs/wtf",
                         reduce_file_path("/srv/www/htdocs/wtf/"))
        # "/srv/www/htdocs/wtf"
        self.assertEqual("/srv/www/htdocs", reduce_file_path("/srv/www/htdocs/wtf"))
        # "/srv/www/htdocs/wtf"
        self.assertEqual("/srv", reduce_file_path("/srv/./././././"))
        # "/srv"
        self.assertEqual("/etc/wtf", reduce_file_path("/etc//wtf/"))
        # "/etc/wtf"
        self.assertEqual("/", reduce_file_path("/etc/../etc/../etc/../"))
        # "/"
        self.assertEqual("/", reduce_file_path("//////////////"))
        # "/"
        self.assertEqual("/", reduce_file_path("/../"))
        # "/"


# Program Run
if __name__ == '__main__':
    unittest.main()
