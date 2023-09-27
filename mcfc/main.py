"""
MCFC
~~~~~~~~~~~~~~~~~~~

🖌 Text formatting using Minecraft color codes.

:copyright: (c) 2023 woidzero
:license: MIT, see LICENSE for more details.
"""

import os
import sys

from mcfc.colors import CODES, Format


def fmt(
    *values: object,
    sep: str = " ",
) -> str:
    """Returns formatted values.

    Parameters
    ----------
    sep (Optional[:class:`str`])
        String inserted between values, default a space.
    """
    text = sep.join(tuple(map(str, values)))

    for code in CODES.items():
        color_code: str = code[0]
        text: str = text.replace(color_code, Format.RESET + CODES[color_code])

    return str(text) + Format.RESET


def echo(
    *values: object,
    sep: str = " ",
    end: str = "\n",
) -> None:
    """Prints the formatted text.

    Parameters
    ----------
    sep (Optional[:class:`str`])
        String inserted between values, default a space.
    end (Optional[:class:`str`])
        String appended after the last value, default a newline.
    """
    if sys.platform.lower() == "win32":
        os.system("color")

    sys.stdout.write(fmt(*values, sep=sep) + end)


def info() -> None:
    """
    Prints all available formatting and color codes.
    """
    echo(
        """
    Text must be formatted with an ampersand (&).
    Default formatting codes:
    
    &00            &88            &77            &ff
    &11            &99            &22            &aa
    &33            &bb            &44            &cc
    &55            &dd            &66            &ee
    &rr (reset)&r                 &ll (bold)&r
    &nn (underline)&r             &oo (italic)&r
    &mm (strikethrough)&r

    ----- Custom formatting codes (not widely supported):
    &jj (blink)&r                 &pp (overline)&r
    &ww (double underline)&r      &ii (invert)&r
    """
    )
