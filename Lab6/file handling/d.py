import os

with open('test.txt', 'r') as file:
    print(len(file.readlines()))