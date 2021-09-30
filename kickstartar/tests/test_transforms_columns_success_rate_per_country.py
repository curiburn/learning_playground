from os import name
import unittest
import pandas as pd

from transforms.columns.success_rate_per_country import column_success_rate_per_country


class TestSuccessRatePerCountry(unittest.TestCase):
    def test_main(self):
        """メインのテスト"""
        actual = column_success_rate_per_country(
            pd.DataFrame(
                {
                    "ID": [1, 2, 3, 4],
                    "is_success": [True, False, True, False],
                    "country": [
                        "Country50",
                        "Country50",
                        "CountryOnlySuccess",
                        "CountryOnlyFail",
                    ],
                }
            )
        )
        expected = pd.Series(
            data=[0.5, 1.0, 0.0],
            index=pd.Index(
                ["Country50", "CountryOnlySuccess", "CountryOnlyFail"], name="country"
            ),
            name="success_rate",
        )

        pd.testing.assert_series_equal(actual.sort_index(), expected.sort_index())
