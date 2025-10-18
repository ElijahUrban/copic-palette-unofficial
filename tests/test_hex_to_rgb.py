import unittest
from copic_palette_unofficial import ColorSymbol


class Test_Hex_To_RGB(unittest.TestCase):

    def test_BV0000_RGB(self):
        color = ColorSymbol.BV0000
        self.assertEqual(color.rgb(), (232, 226, 239))

    def test_BV34_RGB(self):
        color = ColorSymbol.BV34
        self.assertEqual(color.rgb(), (109, 110, 159))


if __name__ == "__main__":
    unittest.main()
