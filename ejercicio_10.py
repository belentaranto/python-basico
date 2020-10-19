abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vocals = ["a", "e", "i", "o", "u"]

abc2 = abc.copy()

for i in abc2:
    for vocal in vocals:
        if i == vocal:
            abc2.remove(i)

print(abc2)