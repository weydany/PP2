def volume_sphere(r: float):
    from math import pi
    return (4 / 3) * pi * r**3

r = float(input())
print(volume_sphere(r))
print('but sphere has no volume :)')