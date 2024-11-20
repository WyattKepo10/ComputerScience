from adafruit_circuitplayground import cp        

while True:
    x, y, z = cp.acceleration
    print("X:", x, "Y:", y, "Z:", z)

    if x > 5:
        cp.pixels[1] = (0,10,0)
        cp.pixels[2] = (0,10,0)
        cp.pixels[3] = (0,10,0)
        cp.pixels[6] = (0,0,0)
        cp.pixels[7] = (0,0,0)
        cp.pixels[8] = (0,0,0)
    elif x < -5:
        cp.pixels[1] = (0,0,0)
        cp.pixels[2] = (0,0,0)
        cp.pixels[3] = (0,0,0)
        cp.pixels[6] = (10,0,0)
        cp.pixels[7] = (10,0,0)
        cp.pixels[8] = (10,0,0)