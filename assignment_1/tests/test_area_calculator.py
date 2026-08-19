"""Tests for the area calculation module."""

import math
import unittest

from area_calculator import (
    calculate_area,
    circle_area,
    rectangle_area,
    square_area,
    triangle_area,
)


class AreaFormulaTests(unittest.TestCase):
    def test_square_area(self) -> None:
        self.assertEqual(square_area(2), 4.0)

    def test_rectangle_area(self) -> None:
        self.assertEqual(rectangle_area(3, 4), 12.0)

    def test_triangle_area(self) -> None:
        self.assertEqual(triangle_area(6, 4), 12.0)

    def test_circle_area_uses_diameter(self) -> None:
        self.assertAlmostEqual(circle_area(2), math.pi)


class AreaDispatcherTests(unittest.TestCase):
    def test_dispatches_every_supported_shape(self) -> None:
        cases = (
            ("square", {"side": 2}, 4.0),
            ("rectangle", {"length": 3, "width": 4}, 12.0),
            ("triangle", {"base": 6, "height": 4}, 12.0),
            ("circle", {"diameter": 2}, math.pi),
        )

        for shape_type, dimensions, expected in cases:
            with self.subTest(shape_type=shape_type):
                self.assertAlmostEqual(
                    calculate_area(shape_type, dimensions), expected
                )

    def test_rejects_unknown_shape(self) -> None:
        with self.assertRaisesRegex(ValueError, "unsupported shape type"):
            calculate_area("hexagon", {"side": 2})

    def test_reports_missing_dimension(self) -> None:
        with self.assertRaisesRegex(ValueError, "width"):
            calculate_area("rectangle", {"length": 3})

    def test_rejects_non_positive_dimensions(self) -> None:
        for invalid_value in (0, -1):
            with self.subTest(value=invalid_value):
                with self.assertRaisesRegex(ValueError, "greater than zero"):
                    calculate_area("square", {"side": invalid_value})

    def test_rejects_non_finite_dimensions(self) -> None:
        for invalid_value in (math.inf, -math.inf, math.nan):
            with self.subTest(value=invalid_value):
                with self.assertRaisesRegex(ValueError, "finite"):
                    calculate_area("circle", {"diameter": invalid_value})

    def test_rejects_non_numeric_dimensions(self) -> None:
        for invalid_value in ("2", True, None):
            with self.subTest(value=invalid_value):
                with self.assertRaisesRegex(ValueError, "must be a number"):
                    calculate_area("square", {"side": invalid_value})


if __name__ == "__main__":
    unittest.main()
