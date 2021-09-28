import datetime
import unittest
import pandas as pd
from transforms.dataframes.preprocess import dataframe_preprocess


class TestPreprocess(unittest.TestCase):
    def test_main(self):
        """メインのテスト"""

        actual = dataframe_preprocess(
            pd.DataFrame(
                {
                    "launched": [
                        "2015-08-11T12:12:28+0000",
                        "2012-07-11T11:13:28+0000",
                    ],
                    "deadline": ["2015-09-11", "2013-07-11"],
                }
            )
        )
        expected = pd.DataFrame(
            {
                "launched": [
                    datetime.datetime(
                        2015,
                        8,
                        11,
                        12,
                        12,
                        28,
                        tzinfo=datetime.timezone(datetime.timedelta(hours=0)),
                    ),
                    datetime.datetime(
                        2012,
                        7,
                        11,
                        11,
                        13,
                        28,
                        tzinfo=datetime.timezone(datetime.timedelta(hours=0)),
                    ),
                ],
                "deadline": [
                    datetime.date(2015, 9, 11),
                    datetime.date(2013, 7, 11),
                ],
            }
        )

        pd.testing.assert_frame_equal(actual, expected)

    def test_invalid(self):
        """エラーを出すテスト"""
        origin = pd.DataFrame(
            {
                "launched": [
                    "2015-08-11T12:12:28+0000",
                    "2012-07-11T11:13:28+0000",
                ],
                "deadline": ["2015-09-11", "2013-07-11"],
            }
        )

        cases = {
            "invalid_lauched__all_zero": origin.append(
                {"launched": "0000-00-00T00:00:00+0000", "deadline": "2021-01-01"},
                ignore_index=True,
            ),
            "invalid_lauched__does_not_exist": origin.append(
                {"launched": "2021-02-30T00:00:00+0000", "deadline": "2021-01-01"},
                ignore_index=True,
            ),
            "invalid_lauched__null": origin.append(
                {"launched": None, "deadline": "2021-01-01"},
                ignore_index=True,
            ),
            "invalid_deadline__all_zero": origin.append(
                {"launched": "2021-01-01T00:00:00+0000", "deadline": "0000-00-00"},
                ignore_index=True,
            ),
            "invalid_deadline__does_not_exist": origin.append(
                {"launched": "2021-01-01T00:00:00+0000", "deadline": "2021-02-31"},
                ignore_index=True,
            ),
            "invalid_deadline__null": origin.append(
                {"launched": "2021-01-01T00:00:00+0000", "deadline": None},
                ignore_index=True,
            ),
        }

        for name, df in cases.items():
            with self.subTest(case=name):
                with self.assertRaises(ValueError):
                    dataframe_preprocess(df)
