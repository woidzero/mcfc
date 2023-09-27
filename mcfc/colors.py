"""
MCFC
~~~~~~~~~~~~~~~~~~~

🖌 Text formatting using Minecraft color codes.

:copyright: (c) 2023 woidzero
:license: MIT, see LICENSE for more details.
"""
from dataclasses import dataclass


@dataclass
class Color:
    """Minecraft color codes"""

    BLACK = "\x1b[30m"
    WHITE = "\x1b[97m"
    DARK_RED = "\x1b[31m"
    DARK_GREEN = "\x1b[32m"
    DARK_YELLOW = "\x1b[33m"
    DARK_BLUE = "\x1b[34m"
    DARK_PURPLE = "\x1b[35m"
    DARK_AQUA = "\x1b[36m"
    GRAY = "\x1b[37m"
    DARK_GRAY = "\x1b[90m"

    RED = "\x1b[91m"
    GREEN = "\x1b[92m"
    YELLOW = "\x1b[93m"
    BLUE = "\x1b[94m"
    PURPLE = "\x1b[95m"
    AQUA = "\x1b[96m"


@dataclass
class Format:
    """Minecraft formatting codes"""

    OBFUSCATED = "\x1b[8m"
    BOLD = "\x1b[1m"
    STRIKETHROUGH = "\x1b[9m"
    UNDERLINE = "\x1b[4m"
    ITALIC = "\x1b[3m"
    RESET = "\x1b[0m"

    BLINK = "\x1b[5m"
    OVERLINE = "\x1b[53m"
    DOUBLE_UNDERLINE = "\x1b[21m"
    INVERT = "\x1b[7m"


CODES = {
    "&0": Color.BLACK,
    "&f": Color.WHITE,
    "&8": Color.DARK_GRAY,
    "&7": Color.GRAY,
    "&1": Color.DARK_BLUE,
    "&9": Color.BLUE,
    "&2": Color.DARK_GREEN,
    "&a": Color.GREEN,
    "&3": Color.DARK_AQUA,
    "&b": Color.AQUA,
    "&4": Color.DARK_RED,
    "&c": Color.RED,
    "&5": Color.DARK_PURPLE,
    "&d": Color.PURPLE,
    "&6": Color.DARK_YELLOW,
    "&e": Color.YELLOW,
    "&r": Format.RESET,
    "&l": Format.BOLD,
    "&n": Format.UNDERLINE,
    "&m": Format.STRIKETHROUGH,
    "&o": Format.ITALIC,
    "&k": Format.OBFUSCATED,
    "&j": Format.BLINK,
    "&p": Format.OVERLINE,
    "&w": Format.DOUBLE_UNDERLINE,
    "&i": Format.INVERT,
}
