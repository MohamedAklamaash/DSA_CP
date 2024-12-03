
def isBalanced(s):
    # Write your code here
    matchbr = {"(":")","{":"}","[":"]"}
    stack = []
    for i,c in enumerate(s):
        if c in matchbr.keys():
            stack.append(c)
        elif c in matchbr.values():
            if stack and c == matchbr[stack[-1]]:
                stack.pop()
            else:
                return 'NO'
    return "YES" if not stack else "NO"


