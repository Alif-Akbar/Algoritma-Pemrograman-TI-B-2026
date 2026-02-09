import math

def cartesian_to_polar(x1, x2, y1, y2):
    """
    Convert Cartesian coordinates (x, y) to polar coordinates (r, theta).
    
    Parameters:
    x1 (float): The x-coordinate in Cartesian system.
    x2 (float): The x-coordinate in Cartesian system.
    y1 (float): The y-coordinate in Cartesian system.
    y2 (float): The y-coordinate in Cartesian system.
    
    Returns:
    tuple: A tuple containing the radius r and angle theta in radians.
    """
    r = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    theta = math.atan2(y2-y1, x2-x1)
    return r, theta

x1 = float(input("Masukkan koordinat x1: "))
y1 = float(input("Masukkan koordinat y1: "))
x2 = float(input("Masukkan koordinat x2: "))
y2 = float(input("Masukkan koordinat y2: "))

r, theta = cartesian_to_polar(x1, y1, x2, y2)
print(f"Koordinat polar: r = {r}, theta = {theta} radian")
