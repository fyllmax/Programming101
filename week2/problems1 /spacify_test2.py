import unittest
import spacify
import os


class test_spacify(unittest.TestCase):

    """Testing the unit"""

    def test_text_spacify(self):

        fileOP = "text_spec.txt"
        nt = open(fileOP, "w+")

        nt.write("hello		wold		and			others")

        nt.close()

        spacify.spacify(fileOP)

        nt = open(fileOP, "r")

        result = nt.read()

        expected = "hello    world    and    others"

        self.assertEqual(expected, result)

        os.remove(fileOP)


if __name__ == '__main__':
    unittest.main()
