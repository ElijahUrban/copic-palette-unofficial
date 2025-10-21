from enum import StrEnum
from .color_utils import hex_to_hsl, hex_to_rgb


class ColorSymbol(StrEnum):

    def hsl(self):
        return hex_to_hsl(str(self))

    def rgb(self):
        return hex_to_rgb(str(self))

    BV0000 = "#e8e2ef"
    """Pale Thistle"""
    BV000 = "#dbbfe7"
    """Iridescent Mauve"""
    BV00 = "#d0b1de"
    """Mauve Shadow"""
    BV01 = "#a19ad8"
    """Viola"""
    BV02 = "#8982d4"
    """Prune"""
    BV04 = "#344290"
    """Blue Berry"""
    BV08 = "#34255d"
    """Blue Violet"""
    BV11 = "#a18dc3"
    """Soft Violet"""
    BV13 = "#626ec4"
    """Hydrangea Blue"""
    BV17 = "#585d83"
    """Deep Reddish Blue"""
    BV20 = "#a4a8c4"
    """Dull Lavender"""
    BV23 = "#777489"
    """Grayish Lavender"""
    BV25 = "#4c4959"
    """Grayish Violet"""
    BV29 = "#13161e"
    """Slate"""
    BV31 = "#c0b9e1"
    """Pale Lavender"""
    BV34 = "#6d6e9f"
    """Bluebell"""
