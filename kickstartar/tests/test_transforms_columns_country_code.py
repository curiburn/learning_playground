import unittest
import pandas as pd

from transforms.columns.country_code import column_country_code


class TestCountryCode(unittest.TestCase):
    def test_main(self):
        """メインのテスト"""
        actual = column_country_code(
            pd.DataFrame({"country": ["Australia", "Austria", "Belgium", "NoNamed"]})
        )
        expected = pd.Series(["AUS", "AUT", "BEL", None], name="country_code")

        pd.testing.assert_series_equal(actual, expected)
