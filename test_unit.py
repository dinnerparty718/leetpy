'''

python -m unittest

test all file name starts with test

'''

import unittest
import tst_script


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        result = tst_script.do_stuff(8)
        self.assertEqual(result, 13)

    def test_do_stuff2(self):
        result = tst_script.do_stuff('efef')
        #self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)


if __name__ == '__main__':
    unittest.main()
