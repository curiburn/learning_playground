"""カラム ペア
"""
import pandas as pd

from transforms.arg_map import BOOL_MAP

def column_is_pair(df: pd.DataFrame) -> pd.Series:
    if "SibSp" not in df:
        raise ValueError("`SibSp` column is needed")
    
    if df.SibSp.isna().any():
        raise ValueError("NaN")
    
    return df.SibSp.apply(
        lambda x: BOOL_MAP.get_int(x == 1)
    ).rename("IsPair")
