import math

def CelToFahr(celsius):
    return (celsius * 9/5) + 32

def min(a, b):
    return a if a < b else b

def VolumeOfSphere(radius):
    return (4/3) * math.pi * (radius ** 3)


if __name__ == "__main__":
    print("CelToFahr(0):", CelToFahr(0))        
    print("min(3, 7):", min(3, 7))             
    print("VolumeOfSphere(1):", VolumeOfSphere(1))  
