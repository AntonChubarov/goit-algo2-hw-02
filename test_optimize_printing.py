import unittest

from optimize_printing import optimize_printing


class TestOptimizePrinting(unittest.TestCase):
    def setUp(self):
        self.constraints = {
            "max_volume": 300,
            "max_items": 2
        }

        self.test_cases = [
            {
                "name": "Same priority tasks",
                "input": [
                    {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
                    {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
                    {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
                ],
                "expected": {
                    "print_order": ["M3", "M1", "M2"],
                    "total_time": 240
                }
            },
            {
                "name": "Different priorities",
                "input": [
                    {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
                    {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
                    {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
                ],
                "expected": {
                    "print_order": ["M2", "M1", "M3"],
                    "total_time": 270
                }
            },
            {
                "name": "Exceeding volume constraints",
                "input": [
                    {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
                    {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
                    {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
                ],
                "expected": {
                    "print_order": ["M1", "M2", "M3"],
                    "total_time": 450
                }
            }
        ]

    def test_optimize_printing(self):
        for case in self.test_cases:
            with self.subTest(case=case["name"]):
                result = optimize_printing(case["input"], self.constraints)
                self.assertEqual(result, case["expected"])


if __name__ == "__main__":
    unittest.main()
