import os

print('Exist:', os.access('test.txt', os.F_OK))
print('Readable:', os.access('text.txt', os.R_OK))
print('Writable:', os.access('text.txt', os.W_OK))
print('Executable:', os.access('test.txt', os.X_OK))