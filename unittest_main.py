import unittest
import main


class MainTest(unittest.TestCase):

    def setUp(self) -> None:
        self.test_dict = {'4': 0, '6': 5, '8': 0, '10': 2, '12': 0, '20': 1, '100': 0}
        self.no_z_dict = {'6': 5, '10': 2, '20': 1}

    def test_reload_dict(self):
        # self.test_dict.reload_dict()
        test_dict = {'4': 0, '6': 5, '8': 0, '10': 2, '12': 0, '20': 1, '100': 0}
        no_z_dict = {'6': 5, '10': 2, '20': 1}
        test = main.reload_dict(test_dict)
        self.assertEqual(test, no_z_dict, 'THERE ARE ZEROS IN DICTIONARY')


if __name__ == '__main__':
    unittest.main()
