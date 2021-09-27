from transforms.columns.is_success import column_is_success
import unittest
import pandas as pd


class TestIsSuccess(unittest.TestCase):
    def test_invalid_case(self):
        """エラーを出す場合のテスト"""
        origin = pd.DataFrame({"ID": [1, 2], "status": ["successful", "failed"]})
        cases = {
            "invalid_string_on_status": origin.append(
                [
                    {"ID": 3, "status": "canceled"},
                    {"ID": 4, "status": "IAmInvalidStatus"},
                ],
                ignore_index=True,
            ),
            "null_status": origin.append({"ID": 3, "status": None}, ignore_index=True),
            "no_status_column": origin.drop("status", axis=1),
        }

        for name, case in cases.items():
            with self.subTest(case=name):
                with self.assertRaises(
                    ValueError,
                ):
                    column_is_success(case)

    def test_main(self):
        """メインのテスト"""
        actual = column_is_success(pd.DataFrame({"status": ["successful", "failed"]}))

        pd.testing.assert_series_equal(
            actual, pd.Series([True, False], name="is_success")
        )
