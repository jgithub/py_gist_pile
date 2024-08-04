import datetime
import json
import re
from typing import Pattern


def d4l(input: any):
    """decorate-for-logging"""

    if input is None:
        return "<null> (null)"
    elif input is None:
        return "<undefined> (undefined)"
    elif isinstance(input, str):
        return f"'{input}' (string, {len(input)})"
    elif isinstance(input, int) or isinstance(input, float):
        return f"{input} (number)"
    elif isinstance(input, bool):
        return "TRUE (boolean)" if input else "FALSE (boolean)"
    elif isinstance(input, dict) or isinstance(input, list):
        try:
            return json.dumps(input)
        except Exception:
            pass
    elif isinstance(input, list):
        parts = []

        input_as_list = input
        if len(input_as_list) > 0:
            parts.append(d4l(input_as_list[0]))
        if len(input_as_list) > 2:
            parts.append("…")
        if len(input_as_list) > 1:
            parts.append(d4l(input_as_list[-1]))

        return f"Array(len={len(input_as_list)}) [{', '.join(parts)}]"
    elif isinstance(input, Exception):
        stack_str = str(input)
        if hasattr(input, "stack"):
            stack_str = (
                input.stack.replace("\r\n", "\\n,   ")
                .replace("\n\r", "\\n,   ")
                .replace("\n", "\\n,   ")
                .replace("\r", "\\n,   ")
            )
        return f"{input} (Error, stack: {stack_str})"
    elif isinstance(input, datetime.datetime):
        return input.isoformat()

    return str(input)


def d4l_secret(obj: any):
    working_d4l = d4l(obj)

    if working_d4l == '<undefined> (undefined)':
        return "<*********> (*********)"
    if working_d4l == '<null> (null)':
        return '<****> (****)'
    if working_d4l == "'' (string)":
        return "/^$/"


    typeof_orig = ""

    if isinstance(working_d4l, str):
        pattern: Pattern = ' \(string, \d+\)$'
        match: Match = re.search(pattern, working_d4l)

        if (match != None):
            working_d4l = re.sub(pattern, "", working_d4l)
            typeof_orig = "string"
        elif working_d4l.endswith(' (string)'):
            working_d4l = working_d4l[:-10]
            working_d4l = working_d4l.lstrip("'").rstrip("'")
            typeof_orig = "string"
        elif working_d4l.endswith(' (number)'):
            working_d4l = working_d4l[:-10]
            typeof_orig = "number"

        # Redeclare
        pattern: Pattern = "^\'(.*)\'$"
        # print(f"working_d4l = {working_d4l}")
        match: Match = re.search(pattern, working_d4l)
        if (match != None):
            # print(f"MATCH")
            working_d4l = match.group(1)
            # print(f"working_d4l = {working_d4l}")

        real_length = len(working_d4l)
        # print(f"real_length = {real_length}")


        quote = "'" if typeof_orig == 'string' else ""

        if len(working_d4l) > 8:
            first_few = working_d4l[:2]
            last_few = working_d4l[-2:]
            working_d4l = f"{quote}{first_few}...{last_few}{quote} ({'string, ' if typeof_orig == 'string' else ''}{real_length})"
        elif len(working_d4l) > 6:
            first_few = working_d4l[:1]
            last_few = working_d4l[-1:]
            working_d4l = f"{quote}{first_few}...{last_few}{quote} ({'string, ' if typeof_orig == 'string' else ''}{real_length})"
        else:
            first_char = working_d4l[:1]
            working_d4l = f"{quote}{first_char}...{quote} ({'string, ' if typeof_orig == 'string' else ''}{real_length})"

    return working_d4l