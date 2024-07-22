from copy import deepcopy
from typing import Any, List, Dict, Union


def recursively_filter_properties_in_place(obj: Any, list_of_property_names_to_remove: List[str]) -> None:
    if isinstance(obj, list):
        for item in obj:
            recursively_filter_properties_in_place(
                item, list_of_property_names_to_remove
            )
    elif isinstance(obj, dict):
        keys = list(obj.keys())
        for key in keys:
            if key in list_of_property_names_to_remove:
                del obj[key]
            else:
                recursively_filter_properties_in_place(
                    obj[key], list_of_property_names_to_remove
                )


def recursively_filter_properties_copy(obj: Any, list_of_property_names_to_remove: List[str]) -> Any:
    clone = deepcopy(obj)
    recursively_filter_properties_in_place(clone, list_of_property_names_to_remove)
    return clone
