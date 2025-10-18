from enum import StrEnum
from .color_utils import hex_to_hsl, hex_to_rgb


class ColorSymbol(StrEnum):

    def hsl(self):
        return hex_to_hsl(str(self))

    def rgb(self):
        return hex_to_rgb(str(self))

    BV0000 = "#e8e2ef"
    """Pale Thistle"""

    BV34 = "#6d6e9f"
    """Bluebell"""
