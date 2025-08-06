import random
g = 0
v = 0
c = 0
def V():
    global v
    global g
    v = v + 1
    if g > 1:
        print(f"Vowels: {v} Consonants: {c}")
        return 0
    i = random.random()
    if i < 0.13:
        V()
        g += 1
    else:
        C()
        g += 1
def C():
    global c
    global g
    c += 1
    if g > 1:
        print(f"Vowels: {v} Consonants: {c}")
        return 0
    i = random.random()
    if i < 0.33:
        C()
        g += 1
    else:
        V()
        g += 1

V()