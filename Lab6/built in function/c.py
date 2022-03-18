s = 'aboba'
if s == ''.join(reversed(s)):
    print('palindrome')
else:
    print('not palindrome')