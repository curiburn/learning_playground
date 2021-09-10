import unittest

import pandas as pd

from transforms.column_is_pair import column_is_pair


class testIsPair(unittest.TestCase):
    def test_example(self):
        """例なデータでのテスト"""
        pd.testing.assert_series_equal(
            column_is_pair(
                pd.DataFrame({"SibSp": [0, 1, 2, 3, 10], "Survived": [1, 0, 1, 0, 1]})
            ),
            pd.Series([0, 1, 0, 0, 0], name="IsPair"),
        )
    
    def test_error(self):
        """エラーを出す場合のテスト"""
        origin = pd.DataFrame({"SibSp": [0, 1, 2, 3, 10], "Survived": [1, 0, 1, 0, 1]})
        cases = {
            "no_SibSp": origin.drop("SibSp", axis=1),
            "has_na": origin.append(
                {"SibSp": float("nan"), "Survived": 1}, ignore_index=True
            )
        }

        for name, df in cases.items():
            with self.subTest(name):
                with self.assertRaises(ValueError):
                    column_is_pair(df)

