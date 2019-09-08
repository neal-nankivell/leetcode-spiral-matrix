import solution
import unittest


class Test_TestSolution(unittest.TestCase):
    def setUp(self):
        self.sut = solution.Solution()

    def test_foo(self):
        input = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expectedOutput = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(self.sut.spiralOrder(input), expectedOutput)


if __name__ == '__main__':
    unittest.main()
