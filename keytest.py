
complexities =   {"A+": 0,
                      "A":  1,
                      "B":  2,
                      "C":  3,
                      "D":  4,
                      "E":  5,
                      "F":  6,
                      "G":  7,
                      "H":  8,}

temp = list(complexities.items())
res = [idx for idx, key in enumerate(temp) if key[0] == "H"]
print(res[0])