import unittest
import pandas as pd
from transforms.column_int_sex import column_int_sex


class testIntSex(unittest.TestCase):
    def test_main(self):
        """メインのテスト"""

        pd.testing.assert_series_equal(
            column_int_sex(
                pd.DataFrame(
                    {"PassengerId": [1, 2, 3], "Sex": ["male", "female", "female"]}
                )
            ),
            pd.Series([0, 1, 1], name="IntSex"),
        )

    def test_error(self):
        """エラーになるケースのテスト"""
        origin = pd.DataFrame(
            {"PassengerId": [1, 2, 3], "Sex": ["male", "female", "female"]}
        )
        cases = {
            "no_Sex_column": origin.drop("Sex", axis=1),
            "unknown_value": origin.append(
                {"PassengerId": 4, "Sex": "aaaa"}, ignore_index=True
            ),
            "na_value": origin.append(
                {"PassengerId": 4, "Sex": None}, ignore_index=True
            ),
        }

        for name, case in cases.items():
            with self.subTest(name):
                with self.assertRaises(ValueError):
                    column_int_sex(case)
