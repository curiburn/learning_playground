import pandas as pd


def column_success_rate_per_country(df: pd.DataFrame) -> pd.Series:
    """国別成功率

    NOTE: 元データとindexが異なるので注意

    Args:
        df (pd.DataFrame): 元データ(PJ別のデータ)

    Returns:
        pd.Series: 集計結果
    """

    if {"country", "is_success"} - set(df.columns) != set():
        raise ValueError("`country` and `is_success` columns not found")

    return (
        df[["country", "is_success"]]
        # 国毎に成功PJ数と失敗PJ数を集計
        .groupby("country").apply(
            lambda x: (x.groupby("is_success").country.count().to_dict())
        )
        # 集計した成功・失敗PJ数から割合を計算
        .apply(lambda x: x.get(True, 0) / (x.get(False, 0) + x.get(True, 0)))
        # 列名
        .rename("success_rate")
    )
