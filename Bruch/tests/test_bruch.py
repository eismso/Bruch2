import unittest

from bruch.bruch import Bruch


class BruchTest(unittest.TestCase):
    def setUp(self) -> None:
        self.bruch1 = Bruch(1, 2)
        self.bruch2 = Bruch(2, 3)
        self.bruch3 = Bruch(3, 4)

    def test_add(self):
        erg1 = self.bruch1.add(self.bruch2)
        erg2 = self.bruch2.add(self.bruch3)
        self.assertEqual(erg1.zaehler, 7, "Addition Zähler")
        self.assertEqual(erg1.nenner, 6, "Addition Nenner")

        self.assertEqual(erg2.zaehler, 17 , "Addition Zähler")
        self.assertEqual(erg2.nenner, 12, "Addition Nenner")

    def test_multiply(self):
        erg1 = self.bruch1.multiply(self.bruch2)
        erg2 = self.bruch2.multiply(self.bruch3)
        self.assertEqual(erg1.zaehler, 2, "Multi Zähler")
        self.assertEqual(erg1.nenner, 6, "Multi Nenner")

        self.assertEqual(erg2.zaehler, 6, "Multi Zähler")
        self.assertEqual(erg2.nenner, 12, "Multi Nenner")

    def test_decimal(self):
        erg1 = self.bruch1.get_decimal_representation()
        erg2 = self.bruch2.get_decimal_representation()

        self.assertAlmostEqual(erg1, 0.5)
        self.assertAlmostEqual(erg2, 2/3)



if __name__ == '__main__':
    unittest.main()
