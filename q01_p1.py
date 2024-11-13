from collections import Counter
values = {'A':0, 'B':1, 'C':3}
with open("everybody_codes_e2024_q01_p1.txt") as f:
    content = f.read()

c = Counter(content)
print(sum(v*values[k] for k,v in c.items()))


