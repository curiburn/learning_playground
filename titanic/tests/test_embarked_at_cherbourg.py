from transforms.arg_map import BOOL_MAP
from transforms.column_embarked_at_cherbourg import column_embarked_at_cherbourg
import unittest
import pandas as pd


class TestEmbarkedAtCherbourg(unittest.TestCase):
    def test_main(self):
        """メインのテスト"""
        pd.testing.assert_series_equal(
            column_embarked_at_cherbourg(
                pd.DataFrame(
                    {"PassengerId": [1, 2, 3, 4], "Embarked": ["C", "Q", "S", None]}
                )
            ),
            pd.Series([1, 0, 0, 0], name="EmbarkedAtCherbourg"),
        )

    def test_error(self):
        """エラーを出す場合のテスト"""
        origin = pd.DataFrame(
            {"PassengerId": [1, 2, 3, 4], "Embarked": ["C", "Q", "S", None]}
        )
        cases = {
            "no_column": origin.drop("Embarked", axis=1),
            "invalid_value": origin.append(
                {"PassengerId": 5, "Embarked": "IAmInvalidString"}, ignore_index=True
            ),
        }

        for name, df in cases.items():
            with self.subTest(case=name):
                with self.assertRaises(ValueError):
                    column_embarked_at_cherbourg(df)
