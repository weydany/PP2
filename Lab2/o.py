def toInt(s : str):
    pow = len(s) / 3 - 1
    ans = 0
    for i in range(0, len(s), 3):
        digit = s[i: i + 3]
        if digit == 'ZER': ans += 0 * 10**pow
        elif digit == 'ONE': ans += 1 * 10**pow
        elif digit == 'TWO': ans += 2 * 10**pow
        elif digit == 'THR': ans += 3 * 10**pow
        elif digit == 'FOU': ans += 4 * 10**pow
        elif digit == 'FIV': ans += 5 * 10**pow
        elif digit == 'SIX': ans += 6 * 10**pow
        elif digit == 'SEV': ans += 7 * 10**pow
        elif digit == 'EIG': ans += 8 * 10**pow
        elif digit == 'NIN': ans += 9 * 10**pow
        pow -= 1
    return ans

def toStr(n : int):
    ans = ''
    for i in str(int(n)):
        if i == '1': ans += 'ONE'
        elif i == '2': ans += 'TWO'
        elif i == '3': ans += 'THR'
        elif i == '4': ans += 'FOU'
        elif i == '5': ans += 'FIV'
        elif i == '6': ans += 'SIX'
        elif i == '7': ans += 'SEV'
        elif i == '8': ans += 'EIG'
        elif i == '9': ans += 'NIN'
        elif i == '0': ans += 'ZER'
    return ans

a, b = input().split('+')
a, b = toInt(a), toInt(b)
print(toStr(a + b))