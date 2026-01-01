def is_anagram(self, s, t):
    freq_map = {}

    if len(s) == len(t):
        for letter in s.lower():
            if letter not in freq_map:
                freq_map[letter] = -1
            else:
                freq_map[letter] -= 1

            if letter in t.lower():
                if letter not in freq_map:
                    freq_map[letter] = 1
                else:
                    freq_map[letter] += 1

    if -1 not in freq_map.values() and 1 not in freq_map.values():
        return True
    return False