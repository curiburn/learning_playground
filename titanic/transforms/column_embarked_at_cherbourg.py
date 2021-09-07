"""カラム Cherbourg(シェルブール)

シェルブールで乗ったか否か
"""

import pandas as pd
from transforms.arg_map import BOOL_MAP


def column_embarked_at_cherbourg(df: pd.DataFrame) -> pd.Series:
    """EmbarkedAtCherbourgカラム生成

    NOTE:
        - `C, Q, S`以外は通さない
        - NoneはC以外のものとして扱う
    """
    if "Embarked" not in df.columns:
        raise ValueError("`Embarked` column is needed")

    if df.Embarked.dropna().apply(lambda x: x not in {"C", "Q", "S"}).any():
        raise ValueError(f"`C, Q, S or None` is allowed; actual={df.Embarked.unique()}")

    return df.Embarked.apply(lambda x: BOOL_MAP.get_int(x == "C")).rename(
        "EmbarkedAtCherbourg"
    )
