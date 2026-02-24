import math

def angle(t):
    A = math.radians(30)
    omega = 2 * math.pi
    return A * math.sin(omega * t)

def angle2(t):
    A = math.radians(30)
    omega = 2 * math.pi
    return A * math.sin(omega * t + math.pi)

def angle3(t, phase):
    A = math.radians(30)
    omega = 2 * math.pi
    return A * math.sin(omega * t + phase)


