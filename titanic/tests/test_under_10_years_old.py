import unittest
import pandas as pd
from transforms.column_under_10_years_old import column_under_10_years_old
from transforms.arg_map import BOOL_MAP


class TestUnder10YearsOld(unittest.TestCase):
    column_name = "Under10YearsOld"

    def test_example(self):
        """例なデータのテスト（正例）"""
        pd.testing.assert_series_equal(
            pd.Series([1, 0, 0], name=self.column_name),
            column_under_10_years_old(
                pd.DataFrame(
                    {"NotAge": ["hoge", "huga", "hage"], "Age": [5, float("nan"), 85]}
                )
            ),
        )

    def test_Age_not_found(self):
        """Ageカラムが存在しない場合のエラーのテスト"""
        with self.assertRaises(ValueError):
            column_under_10_years_old(
                pd.DataFrame(
                    {
                        "NotAge": ["hoge", "huga", "hage"],
                    }
                )
            )

    def test_all_age(self):
        """0-200才までテスト"""
        ages = list(range(200))
        pd.testing.assert_series_equal(
            pd.Series(
                [BOOL_MAP.get_int(x < 10) for x in ages],
                name=self.column_name,
            ),
            column_under_10_years_old(pd.DataFrame({"Age": ages})),
        )
