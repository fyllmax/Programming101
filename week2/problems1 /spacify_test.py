import unittest
import spacify
import tempfile


class test_spacify(unittest.TestCase):

    """Testing the unit"""

    def test_text_spacify(self):
        nt = tempfile.TemporaryFile()

        nt.write("hello		wold		and			others".encode('utf-8'))

        expected = "hello    world    and    others"

        #content = spacify(nt)

        # nt.close()

        self.assertEqual(expected, spacify.spacify(nt))
        #self.assertEqual(expected, content)
        nt.close()


if __name__ == '__main__':
    unittest.main()
