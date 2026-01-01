def is_palindrome(s) -> bool:
    s = s.lower()
    s = [c for c in s if c.isalnum()]
    s_clean = "".join(s)

    lt = 0
    rt = len(s_clean) - 1
    while lt < rt:
        if s_clean[lt] != s_clean[rt]:
            return False
        lt += 1
        rt -= 1
    return True
