from collections import defaultdict,deque

def wordLadder(start,end,wordList):
    if not start or not end or not wordList:
        return -1
    
    adjlist = defaultdict(list)
    
    for i in range(len(wordList)):
        word = wordList[i]
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j+1:]
            adjlist[pattern].append(word)
    
    queue = deque([(start,0)])
    visited = set([start])
    while queue:
        for i in range(len(queue)):
            word,steps = queue.popleft()
            if word == end:
                return steps+1
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                for neigh in adjlist[pattern]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append((neigh,steps+1))
    return -1

'''
    my leetcode approach
'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        graph = defaultdict(list)
        for i in range(len(wordList)):
            word = wordList[i]
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                graph[pattern].append(word)
        
        queue = deque([(beginWord,0)])
        visited = set([beginWord])
        while queue:
            word,steps = queue.popleft()
            if word == endWord:
                return steps+1
            
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                for neigh in graph[pattern]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append((neigh,steps+1))
        return 0
    
if __name__ == "__main__":
    # Example inputs
    start_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]

    # Solve the word ladder problem
    transformation = wordLadder(start_word, end_word, word_list)
    print(transformation)