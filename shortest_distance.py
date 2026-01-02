def shortestDistance(words, word1, word2):
    pos1, pos2 = -1, -1
    distance = None
    count = 0
    for word in words:
        if word == word1:
            pos1 = count
            print(f"Found {word1} at position {pos1}")
        if word == word2:
            pos2 = count
            print(f"Found {word2} at position {pos2}")
        if pos1 != -1 and pos2 != -1:
            if not distance:
                distance = abs(pos1 - pos2)
            elif distance > abs(pos1 - pos2):
                distance = abs(pos1 - pos2)
        count += 1

    return distance

if __name__ == "__main__":
    words = ["a", "c", "d", "b", "a"]
    word1 = "a" 
    word2 = "b"

    print("Shortest distance:", shortestDistance(words, word1, word2))

