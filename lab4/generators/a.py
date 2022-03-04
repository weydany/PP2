# class Iterator:
#     def __iter__(self):
#         self.x = 0
#         return self

#     def __next__(self):
#         ans = self.x**2
#         self.x += 1
#         return ans

# n = int(input())
# ans = Iterator()
# it = iter(ans)

# for _ in range(n + 1):
#     print(next(it))

def generator():
    ans = 1
    while True:
        yield ans**2
        ans += 1

n = int(input())
gen = generator()
for _ in range(n):
    print(next(gen))