from collections import Counter
values = {'xx': 0,'DA': 7, 'AD': 7,'Ax':0, 'xA': 0, 'AA': 2, 'BC':6, 'CB': 6, 'CC': 8, 'BB': 4, 'xB': 1, 'Bx': 1, 'CA':5, 'AC':5, 'AB': 3, 'BA': 3, 'BD': 8, 'DB': 8, 'CD': 10, 'DC':10, 'DD':12, 'xD':5, 'Dx': 5, 'Cx': 3, 'xC': 3}
with open("everybody_codes_e2024_q01_p2.txt") as f:
    content = f.read()

pairs = []
for x in range(0, len(content), 2):
    pairs.append(content[x:x+2])
c = Counter(pairs)
print(sum(v*values[k] for k,v in c.items()))


