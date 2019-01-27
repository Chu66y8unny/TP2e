import math

def sphere_vol(r):
    return 4.0 / 3.0 * math.pi * r**3

if __name__ == '__main__':
    radius = 5
    vol = sphere_vol(radius)
    print(f"The volume of a sphere with radius {radius} is {vol}")
