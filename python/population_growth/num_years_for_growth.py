def nb_year(p0, percent, aug, p):
    percent /= 100
    yr_count = 0

    while p0 < p:
        reg_increase = p0 * percent
        p0 += int(aug + reg_increase)
        yr_count += 1

    return yr_count


if __name__ == "__main__":
    print(nb_year(1500, 5, 100, 5000))  # Output: 15
    print(nb_year(1500000, 2.5, 10000, 2000000))  # Output: 10
    print(nb_year(1500000, 0.25, 1000, 2000000))  # Output: 94
