"""Area calculation functions for the universal area calculator.

All dimensions passed to this module must already be converted to centimeters.
Returned areas are measured in square centimeters and are not rounded here.
"""

from __future__ import annotations

import math
from collections.abc import Callable, Mapping
from numbers import Real


def _validate_length(value: Real, field_name: str) -> float:
    """Return a valid positive, finite length as a float."""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{field_name} must be a number")

    value_as_float = float(value)
    if not math.isfinite(value_as_float):
        raise ValueError(f"{field_name} must be finite")
    if value_as_float <= 0:
        raise ValueError(f"{field_name} must be greater than zero")

    return value_as_float


def square_area(side: Real) -> float:
    """Calculate the area of a square from its side length."""
    side_cm = _validate_length(side, "side")
    return side_cm**2


def rectangle_area(length: Real, width: Real) -> float:
    """Calculate the area of a rectangle from its length and width."""
    length_cm = _validate_length(length, "length")
    width_cm = _validate_length(width, "width")
    return length_cm * width_cm


def triangle_area(base: Real, height: Real) -> float:
    """Calculate the area of a triangle from its base and height."""
    base_cm = _validate_length(base, "base")
    height_cm = _validate_length(height, "height")
    return base_cm * height_cm / 2


def circle_area(diameter: Real) -> float:
    """Calculate the area of a circle from its diameter."""
    diameter_cm = _validate_length(diameter, "diameter")
    return math.pi * (diameter_cm / 2) ** 2


AreaFunction = Callable[..., float]

_AREA_RULES: dict[str, tuple[tuple[str, ...], AreaFunction]] = {
    "square": (("side",), square_area),
    "rectangle": (("length", "width"), rectangle_area),
    "triangle": (("base", "height"), triangle_area),
    "circle": (("diameter",), circle_area),
}


def calculate_area(shape_type: str, dimensions: Mapping[str, Real]) -> float:
    """Calculate an area using the rule selected by ``shape_type``.

    Args:
        shape_type: One of ``square``, ``rectangle``, ``triangle`` or ``circle``.
        dimensions: Required lengths in centimeters, keyed by their field names.

    Returns:
        The unrounded area in square centimeters.

    Raises:
        ValueError: If the shape is unsupported or a required dimension is invalid.
    """
    if shape_type not in _AREA_RULES:
        supported = ", ".join(_AREA_RULES)
        raise ValueError(
            f"unsupported shape type: {shape_type!r}; supported types: {supported}"
        )
    if not isinstance(dimensions, Mapping):
        raise ValueError("dimensions must be a mapping")

    required_fields, area_function = _AREA_RULES[shape_type]
    missing_fields = [field for field in required_fields if field not in dimensions]
    if missing_fields:
        missing = ", ".join(missing_fields)
        raise ValueError(f"missing required dimensions for {shape_type}: {missing}")

    values = [dimensions[field] for field in required_fields]
    return area_function(*values)
