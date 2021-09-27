from transforms.columns.is_success import column_int_is_success, column_is_success
import unittest
import pandas as pd


class TestIsSuccessBase(unittest.TestCase):
    def assert_invalid_case(self, test_function: callable):
        """エラーを出すケースのチェック"""

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
                    test_function(case)


class TestIsSuccess(TestIsSuccessBase):
    def test_invalid_case(self):
        """エラーを出す場合のテスト"""
        self.assert_invalid_case(column_is_success)

    def test_main(self):
        """メインのテスト"""
        actual = column_is_success(pd.DataFrame({"status": ["successful", "failed"]}))

        pd.testing.assert_series_equal(
            actual, pd.Series([True, False], name="is_success")
        )


class TestIntIsSuccess(TestIsSuccessBase):
    def test_invalid_case(self):
        """エラーを出す場合のテスト"""
        self.assert_invalid_case(column_int_is_success)

    def test_main(self):
        """メインのテスト"""
        actual = column_int_is_success(
            pd.DataFrame({"status": ["successful", "failed"]})
        )

        pd.testing.assert_series_equal(actual, pd.Series([1, 0], name="int_is_success"))
