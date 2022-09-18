import unittest


def right_angled(a, b, c):
    if (a * a + b * b == c * c) or (c * c + b * b == a * a) or (a * a + c * c == b * b):
        return True
    else:
        return False


def classify_triangle(a, b, c):
    # didn't add functionality to test if triangle is invalid.
    # This should be caught in the test cases.
    if a == b and b == c:
        w = "Equilateral "
    elif a == b or b == c or a == c:
        w = "Isosceles "
    else:
        w = "Scalene "
    if right_angled(a, b, c):
        w += "and right angled."
    else:
        w += "and not right angled."

    print(w)
    return w


class TestTriangles(unittest.TestCase):
    def testEquilateral(self):
        self.assertEqual(classify_triangle(4, 4, 4), "Equilateral and not right angled.")

    def testIsosceles(self):
        self.assertEqual(classify_triangle(4, 4, 5), "Isosceles and not right angled.")

    def testScalene(self):
        self.assertEqual(classify_triangle(3, 4, 2), "Scalene and not right angled.")

    def testScaleneRight(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene and right angled.")

    def testInvalidTriangle(self):
        self.assertEqual(classify_triangle(4, 10, 5), "Invalid Triangle.")


if __name__ == "__main__":
    unittest.main()
