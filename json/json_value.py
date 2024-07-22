from typing import Union, Dict, List

JsonValue = Union[str, int, float, bool, Dict[str, 'JsonValue'], List['JsonValue']]

