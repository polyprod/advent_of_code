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
    return sum(x < y for x, y in zip(measurements, measurements[1:]))
    
    # zip(measurements, measurements[1:]) looks like this:
    # [(199, 200), (200, 208), (208, 210), (210, 200), (200, 207), (207, 240), (240, 269), (269, 260), (260, 263)]

def main():
    measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    print("Number of times the depth measurement increased: %d" % count_increments(measurements))

if __name__ == "__main__":
    main()