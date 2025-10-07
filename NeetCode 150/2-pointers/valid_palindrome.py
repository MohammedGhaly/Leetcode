def isPalindrome(s: str) -> bool:
    new_s = ''.join([ch.lower() for ch in s if ch.isalnum()])
    r = 0
    l = len(new_s) - 1
    while r < l:
        if not new_s[r] == new_s[l]:
            return False
        r += 1
        l -= 1
    return True


string = "A man, a plan, a canal: Panama"
print(isPalindrome(string))
