"""pandararellを使うデコレータ

jupyter用で作られているのでアレだが、initializeを複数実行するのは無駄なので避けたい
"""

from typing import Callable
from functools import wraps
from pandarallel import pandarallel
import pandas as pd


def use_pandarallel(func: Callable):
    """pandarallel使用デコレータ"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        # initializeされていなければinitializeする
        #   XXX: parallel_applyがあるかどうかでinitializeの有無をチェックしているが、もうちょっといいのあれば
        if not hasattr(pd.DataFrame, "parallel_apply"):
            pandarallel.initialize()

        return func(*args, **kwargs)

    return wrapper
