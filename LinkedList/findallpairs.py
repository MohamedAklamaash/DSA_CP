
def findallPairs(head,k):
    freq = {}
    curr = head
    res = []
    while curr:
        complement = k - curr.val
        if complement in freq:
            res.append((complement,curr.val))
        freq[curr.val] = 1
        curr = curr.next
    return res

