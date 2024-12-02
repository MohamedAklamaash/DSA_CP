
def rabin_karp_search(text, pattern, base=256, prime=101):
    n, m = len(text), len(pattern)
    pattern_hash = 0
    text_hash = 0
    h = 1  # h = base^(m-1) % prime
    positions = []

    # Calculate h = base^(m-1) % prime
    for _ in range(m - 1):
        h = (h * base) % prime

    # Calculate the hash for the pattern and the first window of text
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    # Slide the pattern over text
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            # Confirm by checking characters to handle hash collisions
            if text[i:i + m] == pattern:
                positions.append(i)

        # Update the hash for the next window
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime

    return positions

# Example
text = "ababcabcabababd"
pattern = "ababd"
print("Rabin-Karp matches found at indices:", rabin_karp_search(text, pattern))

