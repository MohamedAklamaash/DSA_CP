from collections import defaultdict, deque

def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    if endWord not in wordList:
        return 0

    # Step 1: Build adjacency list
    wordList.append(beginWord)
    adjacency = defaultdict(list)
    word_length = len(beginWord)

    for word in wordList:
        for i in range(word_length):
            # Create intermediate pattern (e.g., h*t, *ot)
            pattern = word[:i] + '*' + word[i+1:]
            adjacency[pattern].append(word)

    # Step 2: BFS
    queue = deque([(beginWord, 1)])  # (current word, current transformation depth)
    visited = set([beginWord])

    while queue:
        current_word, level = queue.popleft()

        for i in range(word_length):
            pattern = current_word[:i] + '*' + current_word[i+1:]

            for neighbor in adjacency[pattern]:
                if neighbor == endWord:
                    return level + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))

            # Once processed, clear the pattern neighbors to save memory
            adjacency[pattern] = []

    return 0

