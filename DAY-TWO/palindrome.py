def palindrome(string):
    def check(left, right):
        if left >= right:
            return True
        if string[left] != string[right]:
            return False
        return check(left+1, right-1)
    return check(0, len(string)-1)

new_string = 'HOTDOGSGODTOH'
print(palindrome(new_string))
        