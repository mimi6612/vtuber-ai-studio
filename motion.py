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

# 周波数を揺らす
def omega(t):
    base_omega = 2 * math.pi
    fluctuation = 0.5 * math.sin(0.5 * t)  # 周波数の揺らぎ
    return base_omega + fluctuation

def angle4(t):
    A = math.radians(30)
    return A * math.sin(omega(t) * t)


