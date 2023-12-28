"""Test script."""
import os
import sys

import numpy as np


def a_of_c(r: float) -> float:
    """Area of circle.

    Args:
        r (float): _description_

    Returns:
        _type_: _description_
    """
    return r**2 * 3.14


def a_of_t(h: float, w: float) -> float:
    """Area of triangle.

    Args:
        h (float): _description_
        w (float): _description_

    Returns:
        _type_: _description_
    """
    return 0.5 * h * w
