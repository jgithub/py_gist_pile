from typing import Union

from py_gist_pile.jjson.json_object import JsonObject
from py_gist_pile.jjson.json_array import JsonArray


# Define JsonObjectOrArray type
JsonObjectOrArray = Union[JsonObject, JsonArray]
