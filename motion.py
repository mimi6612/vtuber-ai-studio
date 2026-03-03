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

# 振幅を揺らす
def A(t):
    base_A = math.radians(30)
    fluctuation = 0.5 * math.sin(0.5 * t)  # 振幅の揺らぎ
    return base_A + fluctuation

# ノイズを加える
def noise(t):
    return 0.1 * math.sin(5 * t)  # ノイズの例

def angle4(t):
    return A(t) * math.sin(omega(t) * t) + noise(t)  # ノイズを加えた角度

