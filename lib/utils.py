def unquote_string(s: str) -> str:
    if (s[0] == '"' and s[-1] == '"') or (s[0] == "'" and s[-1] == "'") and len(s) > 1:
        return s[1:-1]

    return s
