"""性別をintにするモジュール"""

import pandas as pd

from transforms.arg_map import ColumnBase, ArgMap

INT_SEX = ColumnBase([
    ArgMap("male", 0),
    ArgMap("female", 1),
])

def column_int_sex(df: pd.DataFrame) -> pd.Series:
    if "Sex" not in df.columns:
        raise ValueError
    
    return df.Sex.apply(INT_SEX.get_int).rename("IntSex")
