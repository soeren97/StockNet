import numpy as np


def area_of_circle(radius: float | None = None) -> float:
    """Calculate the area of a circle based on radius

    Args:radius (float | None, optional): Radius of circle. Defaults to None.

    Returns:float: Area of cirlce.
    """
    return radius**2 * 3.14
