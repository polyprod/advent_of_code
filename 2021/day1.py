# --- Day 1: Sonar Sweep ---

# For example, suppose you had the following report:
# 199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263

# Count the number of times a depth measurement increases from the previous measurement.
# (There is no measurement before the first measurement)

def count_increments(measurements):
    ctr = 0

    for i in range(len(measurements)):
        if (i - 1) < 0:
            continue
        
        if measurements[i] > measurements[i - 1]:
            ctr += 1

    return ctr        

def main():
    measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    print("Number of times the depth measurement increased: %d" % count_increments(measurements))

if __name__ == "__main__":
    main()