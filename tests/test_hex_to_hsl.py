import unittest
from copic_palette_unofficial import ColorSymbol


class Test_Hex_To_HSL(unittest.TestCase):

    def test_BV0000_HSL(self):
        color = ColorSymbol.BV0000
        self.assertEqual(color.hsl(), (268, 29, 91))

    def test_BV34_HSL(self):
        color = ColorSymbol.BV34
        self.assertEqual(color.hsl(), (239, 21, 53))


if __name__ == "__main__":
    unittest.main()
