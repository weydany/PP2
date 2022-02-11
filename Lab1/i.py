n = int(input())
for i in range(n):
    s = input()
    if s.find('@gmail.com') != -1:
        print(s[:s.find('@gmail.com')])