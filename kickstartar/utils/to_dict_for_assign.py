import pandas as pd
from typing import Dict


def to_dict_for_assign(series: pd.Series) -> Dict:
    """assignの引数用のseriesの変換関数

    `df.assign(series.name=series)`って重複してseriesを参照するのを避けたい
    用途：`df.assign(**to_dict_for_assign(series))`
    """
    return {series.name: series}
