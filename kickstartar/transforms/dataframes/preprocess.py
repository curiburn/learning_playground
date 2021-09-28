"""前処理モジュール

何の変形・EDAするにせよ、これは処理しておかないとまずいやろ　なカラムの変形を記述
前処理ではカラムごとの変形では実装せず、直接dataframeの変形として実装する
"""

import datetime
import pandas as pd


def _column_datetime_lauched(df: pd.DataFrame) -> pd.Series:
    """launchedがstringなのでparseする"""
    if "launched" not in df.columns:
        raise ValueError("`launched` column not found")

    if df.launched.isna().any():
        raise ValueError("`lauched` column has NULL.")

    return df.launched.apply(
        lambda x: datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S%z")
    ).rename("launched")


def _column_date_deadline(df: pd.DataFrame) -> pd.Series:
    """deadlineがstringなのでparseする"""
    if "deadline" not in df.columns:
        raise ValueError("`launched` column not found")

    if df.deadline.isna().any():
        raise ValueError("`deadline` column has NULL.")

    return df.deadline.apply(
        lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").date()
    ).rename("deadline")


def dataframe_preprocess(df: pd.DataFrame) -> pd.DataFrame:
    return df.assign(
        launched=_column_datetime_lauched(df), deadline=_column_date_deadline(df)
    )
