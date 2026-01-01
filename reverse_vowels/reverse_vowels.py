def reverse_vowels(s):
    vowels = "aeiou"
    s_vowels = [c for c in s if c.lower() in vowels]
    out = []
    for c in s:
        if c.lower() in vowels:
            out.append(s_vowels.pop())
        else:
            out.append(c)
    return "".join(out)
