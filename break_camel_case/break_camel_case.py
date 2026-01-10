def break_camel_case(s):
    str = ""
    if s:
        for c in s:
            if not (c.isupper()):
                str += c
            else: str += ' '+c
    return str