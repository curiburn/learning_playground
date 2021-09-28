"""プロジェクトの期間（日数）カラム
"""

import pandas as pd
from utils.use_pandaralell import use_pandarallel


@use_pandarallel
def column_duration(df: pd.DataFrame) -> pd.Series:
    """プロジェクトの期間（日数）カラム

    Args:
        df (pd.DataFrame): 元データ

    Returns:
        pd.Series: 当該カラム
    """

    if {"launched", "deadline"} - set(df.columns) != set():
        raise ValueError("`launched` and `deadline` columns not found")

    return df.parallel_apply(
        lambda x: (
            pd.to_datetime(x.deadline).replace(tzinfo=x.launched.tzinfo)
            - pd.to_datetime(x.launched)
        ).days,
        axis=1,
    ).rename("duration")
