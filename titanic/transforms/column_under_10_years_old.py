"""カラム 10歳以下
"""

import math
import pandas as pd
from transforms.arg_map import ArgMap, ColumnBase, BOOL_MAP

def column_under_10_years_old(df: pd.DataFrame) -> pd.Series:
    if "Age" not in df.columns:
        raise ValueError(f"`Age` column not found: {df.columns}")
    
    return df.Age.apply(
        lambda age: BOOL_MAP.get_int((not math.isnan(age)) and (0 <= age < 10))
    ).rename("Under10YearsOld")
