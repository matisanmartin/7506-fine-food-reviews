d1 = 0.8
d2 = 0.6
r = 5
b = 3
# p1 = 1 - (1-(1-d1)**r)**b
# p2 = 1 - (1-(1-d2)**r)**b

for r in range(1, 6):
    for b in range(1, 6):
        p1 = 1 - (1 - d1 ** r) ** b
        p2 = 1 - (1 - d2 ** r) ** b
        print('r: ' + str(r) + ' b: ' + str(b) + ' p1: ' + str(p1) + ' p2: ' + str(p2))
