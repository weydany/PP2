def prime(x: int):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def only_primes(a: list):
    ans = []
    for i in a:
        if prime(i):
            ans.append(i)
    return ans

a = list(map(int, input().split()))
print(only_primes(a))