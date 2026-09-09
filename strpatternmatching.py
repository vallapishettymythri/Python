#brute force pattern matching
def pattern_match(string, pattern):
    n = len(string)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0

        while j < m:
            if string[i + j] != pattern[j]:
                break
            j += 1

        if j == m:
            return True, i, i + m - 1

    return False, -1, -1


string = "ababababababbbbbbababb"
pattern = "ababb"

print(pattern_match(string, pattern))