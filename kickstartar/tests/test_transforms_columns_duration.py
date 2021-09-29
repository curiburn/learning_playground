from transforms.columns.duration import column_duration
import datetime
import unittest
import pandas as pd
from tests.utils.constants import UTC


class TestDuration(unittest.TestCase):
    def test_main(self):
        """メインのテスト"""
        actual = column_duration(
            pd.DataFrame(
                {
                    "launched": [
                        datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=UTC),
                    ],
                    "deadline": [datetime.date(2021, 1, 20)],
                }
            )
        )
        expected = pd.Series([19], name="duration")

        pd.testing.assert_series_equal(actual, expected)

    def test_invalid(self):
        """エラーが出るテスト"""
        origin = pd.DataFrame(
            {
                "ID": [1],
                "launched": [
                    datetime.datetime(2021, 1, 1, 0, 0, 0, tzinfo=UTC),
                ],
                "deadline": [datetime.date(2021, 1, 20)],
            }
        )

        cases = {
            "minus_duration": origin.append(
                {
                    "ID": [2],
                    "launched": datetime.datetime(2021, 1, 1, tzinfo=UTC),
                    "deadline": datetime.date(2020, 12, 1),
                },
                ignore_index=True,
            ),
            "invalid_launched__na": origin.append(
                {
                    "ID": [2],
                    "launched": pd.NA,
                    "deadline": datetime.date(2020, 12, 1),
                },
                ignore_index=True,
            ),
            "invalid_deadline__na": origin.append(
                {
                    "ID": [2],
                    "launched": datetime.datetime(2021, 1, 1, tzinfo=UTC),
                    "deadline": pd.NA,
                },
                ignore_index=True,
            ),
            "missing_deadline": origin.drop("deadline", axis=1),
            "missing_launched": origin.drop("launched", axis=1),
            "missing_both": origin.drop(["launched", "deadline"], axis=1),
        }

        for name, df in cases.items():
            with self.subTest(case=name):
                with self.assertRaises(ValueError):
                    column_duration(df)
