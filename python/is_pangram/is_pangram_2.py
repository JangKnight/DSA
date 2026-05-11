def is_pangram(st):
    alpha_arr = []
    st = st.lower()

    for c in st:
        if c.isalpha():
            alpha_arr.append(c)

    if len(set(alpha_arr)) == 26:
        return True
    return False
