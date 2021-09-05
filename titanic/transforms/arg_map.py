from dataclasses import dataclass
from typing import Union, List


@dataclass(frozen=True)
class ArgMap:
    raw_value: Union[str, bool]
    int_value: int


@dataclass(frozen=True)
class ColumnBase:
    columns: List[ArgMap]

    def __post_init__(self):
        if len({x.raw_value for x in self.columns}) != len(self.columns) or len({
            x.int_value for x in self.columns
        }) != len(self.columns):
            raise ValueError("duplicate raw_value or int_value. check the definition")

    def get_int(self, raw_value: Union[str, bool]) -> int:
        filtered = [x for x in self.columns if x.raw_value == raw_value]

        if not filtered:
            raise ValueError(f"raw_value={raw_value} not found")

        return filtered[0].int_value
    
    def get_value(self, int_value: int) -> Union[str, bool]:
        filtered = [x for x in self.columns if x.int_value == int_value]

        if not filtered:
            raise ValueError(f"int_value={int_value} not found")

        return filtered[0].raw_value

BOOL_MAP = ColumnBase([
    ArgMap(True, 1),
    ArgMap(False, 0),
])
