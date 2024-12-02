
def kmp_search(text, pattern):
    # Step 1: Build LPS array
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    # Step 2: Use LPS to search the pattern in text
    lps = build_lps(pattern)
    i = j = 0  # indices for text and pattern
    positions = []  # store positions of matches

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            positions.append(i - j)  # match found
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions

# Example
text = "ababcabcabababd"
pattern = "ababd"
print("KMP matches found at indices:", kmp_search(text, pattern))
