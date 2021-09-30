import pandas as pd
import pycountry
import warnings


def _get_country_code(name: str) -> str:
    """国名から国コードを取得"""
    try:
        countries = pycountry.countries.search_fuzzy(name)
    except LookupError:
        warnings.warn(f"name={name} country not found", UserWarning)
        return None

    if len(countries) != 1:
        warnings.warn(
            f"""
        multiple countries hit
        name={name}
        hit={countries}
        """,
            UserWarning,
        )
    return countries[0].alpha_3


def column_country_code(df: pd.DataFrame) -> pd.Series:
    """ISO-3な国コードを取得

    country列の国名から国コードな列を生成する

    Args:
        df (pd.DataFrame): 元データ

    Returns:
        pd.Series: country code series
    """

    if "country" not in df.columns:
        raise ValueError("`country` column not found")

    return df.country.apply(_get_country_code).rename("country_code")
