"""statusカラムの代わりに成功したかどうかのis_successカラムにする
"""

import pandas as pd
from pandas.core.indexes.api import all_indexes_same

from transforms.columns.is_success import IS_SUCCESS_MAP, column_is_success


def dataframe_is_success(df: pd.DataFrame) -> pd.DataFrame:
    if "status" not in df.columns:
        raise ValueError("`status` column not found")

    # カラムに合わせた値のレコードのみにフィルタ
    filtered = df[df.status.isin(IS_SUCCESS_MAP.keys())].copy()

    # is_successカラムを作成し、statusカラムを削除
    return filtered.assign(is_success=column_is_success(filtered)).drop(
        "status", axis=1
    )
