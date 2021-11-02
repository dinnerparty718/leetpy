'''

test all file name starts with test

python -m unittest


python -m unittest -v

'''

import unittest
import tst_script


class TestMain(unittest.TestCase):

    # apply for test case
    # def setUp(self) -> None:
    #     print('about to run some cool test')

    def test_do_stuff(self):
        result = tst_script.do_stuff(8)
        self.assertEqual(result, 13)

    def test_do_stuff2(self):
        result = tst_script.do_stuff('efef')
        #self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)

    # not too common
    # def tearDown(self) -> None:
    #     print('cleaning up')
    #     return super().tearDown()


if __name__ == '__main__':
    unittest.main()
