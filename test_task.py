import unittest

def check(x):

    return x >= 100


class TestBool(unittest.TestCase):

    def test(self):
        self.assertTrue(check(99), True)

if __name__ == '__main__':

    unittest.main()