import unittest
import Solution


class TestOneChange(unittest.TestCase):

    def test_1018(self):
        solution = Solution.Solution()
        up1 = [2, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 1]
        mid1 = [2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1]
        down1 = [2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1]
        col1 = [4, 4, 0, 0, 1, 3, 3, 2, 2, 2, 3, 2, 3, 0, 3, 4, 3, 3, 3, 3, 1, 3, 4, 2, 3, 2, 3, 0, 0, 1]
        res1 = solution.getMaxScore(30, up1, mid1, down1, col1, 1)
        self.assertEqual(res1, 1018)

    def test_1998(self):
        solution = Solution.Solution()
        up2 = [2, 2, 3, 3, 1, 3, 3, 3, 1, 3, 1, 1, 2, 3, 2, 1, 3, 2, 1, 2, 1, 3, 1, 1, 1, 2, 3, 3, 2, 2]
        mid2 = [3, 3, 3, 3, 1, 1, 2, 2, 2, 3, 3, 1, 1, 3, 1, 3, 2, 1, 3, 3, 2, 2, 3, 3, 3, 3, 1, 1, 3, 2]
        down2 = [3, 3, 1, 2, 1, 2, 1, 2, 3, 3, 2, 3, 2, 1, 2, 2, 2, 2, 3, 3, 2, 1, 3, 3, 3, 1, 3, 1, 2, 2]
        col2 = [2, 0, 4, 0, 4, 1, 1, 2, 1, 1, 1, 0, 4, 1, 1, 2, 4, 4, 2, 2, 4, 3, 2, 1, 3, 1, 2, 0, 0, 0]
        res2 = solution.getMaxScore(30, up2, mid2, down2, col2, 1)
        self.assertEqual(res2, 1998);

    def test_912(self):
        solution = Solution.Solution()
        up3 = [2, 2, 2, 2, 3, 2, 4, 2, 4, 4, 2, 3, 4, 3, 1, 2, 4, 1, 3, 1, 4, 3, 2, 4, 2, 3, 1, 3, 3, 1]
        mid3 = [3, 1, 3, 1, 2, 2, 4, 3, 3, 3, 1, 4, 3, 1, 3, 2, 2, 3, 2, 1, 2, 1, 3, 4, 3, 4, 2, 4, 4, 1]
        down3 = [2, 4, 1, 2, 1, 4, 1, 4, 2, 2, 2, 3, 3, 2, 2, 1, 2, 1, 1, 3, 3, 1, 2, 1, 3, 1, 1, 4, 2, 2]
        col3 = [4, 4, 2, 2, 3, 3, 3, 1, 2, 3, 2, 3, 0, 4, 1, 1, 1, 4, 3, 4, 1, 1, 4, 3, 4, 1, 3, 3, 3, 0]
        res3 = solution.getMaxScore(30, up3, mid3, down3, col3, 1)
        self.assertEqual(res3, 912);

    def test_584(self):
        solution = Solution.Solution()
        up4 = [1, 1, 1, 4, 2, 4, 3, 3, 2, 2, 5, 3, 2, 2, 2, 3, 1, 2, 4, 5, 3, 3, 3, 5, 3, 2, 3, 5, 4, 5]
        mid4 = [2, 5, 3, 2, 5, 4, 4, 4, 2, 5, 2, 1, 5, 4, 1, 3, 5, 3, 2, 2, 1, 1, 3, 1, 3, 4, 2, 3, 4, 5]
        down4 = [4, 1, 5, 4, 5, 3, 5, 4, 2, 5, 5, 5, 4, 3, 2, 3, 5, 5, 4, 4, 3, 3, 5, 4, 2, 4, 5, 4, 2, 1]
        col4 = [1, 1, 0, 2, 2, 3, 4, 0, 1, 3, 0, 2, 1, 4, 4, 2, 4, 1, 3, 1, 2, 0, 0, 3, 0, 3, 3, 4, 4, 2]
        res4 = solution.getMaxScore(30, up4, mid4, down4, col4, 1)
        self.assertEqual(res4, 584)


class TestOneChange2(unittest.TestCase):

    def test_694(self):
        solution = Solution.Solution()
        up1 = [2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 1, 2]
        mid1 = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1]
        down1 = [2, 1, 1, 2, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 1, 1, 2, 1, 1, 2]
        col1 = [1, 4, 4, 2, 3, 1, 4, 2, 3, 1, 0, 1, 0, 1, 4, 1, 2, 0, 3, 1]
        res1 = solution.getMaxScore(20, up1, mid1, down1, col1, 1)
        self.assertEqual(res1, 694)

    def test_1176(self):
        solution = Solution.Solution()
        up2 = [1, 2, 2, 3, 2, 3, 3, 3, 2, 3, 2, 1, 1, 3, 3, 1, 3, 2, 1, 3]
        mid2 = [1, 3, 2, 1, 2, 1, 3, 2, 3, 2, 3, 3, 1, 2, 1, 3, 1, 1, 3, 1]
        down2 = [2, 3, 1, 1, 2, 2, 1, 2, 3, 3, 2, 2, 2, 3, 1, 2, 1, 1, 3, 2]
        col2 = [2, 2, 3, 1, 4, 1, 4, 0, 1, 1, 1, 0, 4, 1, 2, 0, 0, 2, 4, 3]
        res2 = solution.getMaxScore(20, up2, mid2, down2, col2, 1)
        self.assertEqual(res2, 1176)

    def test_725(self):
        solution = Solution.Solution()
        up3 = [4, 1, 4, 3, 2, 4, 1, 2, 4, 4, 2, 1, 2, 3, 3, 4, 4, 1, 1, 4]
        mid3 = [3, 4, 3, 4, 1, 2, 1, 2, 2, 1, 2, 4, 3, 4, 3, 4, 1, 4, 3, 3]
        down3 = [3, 1, 3, 4, 1, 1, 4, 2, 2, 4, 2, 1, 1, 3, 2, 1, 4, 1, 1, 2]
        col3 = [1, 2, 4, 3, 3, 0, 4, 2, 4, 1, 3, 0, 3, 3, 3, 1, 2, 3, 1, 3]
        res3 = solution.getMaxScore(20, up3, mid3, down3, col3, 1)
        self.assertEqual(res3, 725)

    def test_664(self):
        solution = Solution.Solution()
        up4 = [2, 4, 1, 1, 5, 2, 5, 3, 5, 4, 2, 1, 1, 3, 1, 1, 2, 3, 1, 5]
        mid4 = [2, 2, 4, 4, 3, 5, 4, 3, 2, 2, 3, 3, 4, 1, 2, 4, 1, 5, 5, 3]
        down4 = [2, 3, 3, 5, 2, 2, 2, 4, 3, 1, 5, 5, 4, 4, 1, 2, 4, 4, 3, 5]
        col4 = [3, 3, 1, 1, 0, 1, 1, 0, 2, 0, 3, 3, 0, 2, 2, 2, 4, 2, 2, 4]
        res4 = solution.getMaxScore(20, up4, mid4, down4, col4, 1)
        self.assertEqual(res4, 664)


class TestTwoChanges(unittest.TestCase):

    def test_169(self):
        solution = Solution.Solution()
        up1 = [1, 2, 1, 2, 2]
        mid1 = [2, 2, 1, 2, 2]
        down1 = [2, 2, 1, 1, 2]
        col1 = [0, 0, 2, 0, 4]
        res1 = solution.getMaxScore(5, up1, mid1, down1, col1, 2)
        self.assertEqual(res1, 169)

    def test_90(self):
        solution = Solution.Solution()
        up2 = [1, 3, 1, 2, 2]
        mid2 = [2, 3, 2, 3, 2]
        down2 = [2, 3, 2, 3, 3]
        col2 = [3, 1, 0, 1, 0]
        res2 = solution.getMaxScore(5, up2, mid2, down2, col2, 2)
        self.assertEqual(res2, 90)

    def test_90(self):
        solution = Solution.Solution()
        up3 = [2, 3, 1, 2, 1]
        mid3 = [3, 1, 2, 2, 3]
        down3 = [3, 1, 3, 1, 3]
        col3 = [1, 4, 4, 3, 1]
        res3 = solution.getMaxScore(5, up3, mid3, down3, col3, 2)
        self.assertEqual(res3, 90)

    def test_81(self):
        solution = Solution.Solution()
        up4 = [2, 5, 4, 5, 1]
        mid4 = [1, 3, 4, 3, 4]
        down4 = [5, 4, 2, 1, 2]
        col4 = [0, 3, 3, 0, 2]
        res4 = solution.getMaxScore(5, up4, mid4, down4, col4, 2)
        self.assertEqual(res4, 81)


if __name__ == '__main__':
    unittest.main()
