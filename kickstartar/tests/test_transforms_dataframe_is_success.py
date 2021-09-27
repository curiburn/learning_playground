import unittest
import pandas as pd

from transforms.dataframes.is_success import dataframe_is_success


class TestIsSuccess(unittest.TestCase):
    def test_main(self):
        """メインのテスト"""
        actual = dataframe_is_success(
            pd.DataFrame({"ID": [1, 2, 3], "status": ["successful", "failed", "canceled"]})
        )

        pd.testing.assert_frame_equal(
            actual,
            pd.DataFrame({
                "ID": [1,2],
                "is_success": [True, False]
            })
        )
