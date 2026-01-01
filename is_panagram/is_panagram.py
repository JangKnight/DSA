def is_panagram(s):
    alphaSet = set()
    letters = str(s.lower().replace(" ", ""))

    for letter in letters:
        if letter.isalpha():
            alphaSet.add(letter)
    alphaLen = len(alphaSet)
    if alphaLen == 26:
        return True
    return False
