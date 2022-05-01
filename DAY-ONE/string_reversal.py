def solution(s):
    left, right = 0, len(s)-1
    def helper(l, r):
        if l >= r:
            return
        s[l], s[r] = s[r], s[l]
        helper(l+1, r-1)
    helper(left, right)
    return s

def whileSolution(s):
    l, r = 0, len(s)-1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return s

helper = ["h","e","l","l","o","g","i","r","l"]
print(whileSolution(helper))