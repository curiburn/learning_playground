import warnings
import pandas as pd


IS_SUCCESS_MAP = {"successful": True, "failed": False}


def column_is_success(df: pd.DataFrame) -> pd.Series:
    """成功か否かカラム

    Args:
        df (pd.DataFrame): 対象の全体のデータセット

    Returns:
        pd.Series: 成功か否かカラム(bool)
    """

    # statusカラムの存在をチェック
    if "status" not in df.columns:
        raise ValueError("`status` column not found on dataframe.")

    # statusカラムが規定の値のみになっているかチェック
    if set(df.status) - set(IS_SUCCESS_MAP.keys()) != set():
        raise ValueError(
            "`status` has not allowed values"
            f"; allowed values = {IS_SUCCESS_MAP.keys()}"
            f" (actual_values = {df.status.unique()}"
        )

    return df.status.apply(lambda x: IS_SUCCESS_MAP[x]).rename("is_success")
