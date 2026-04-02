import random
v = 0
c = 0
numRec = 0
maxRec = 20
def V():
    global maxRec
    global numRec
    global v

    if numRec > maxRec:
        print(f"Vowels: {v} Consonants: {c}")
        return 0
    v = v + 1
    i = random.random()
    if i < 0.13:

        numRec+=1
        V()

    else:

        numRec+=1
        C()

def C():
    global maxRec
    global numRec
    global c

    if numRec > maxRec:
        print(f"Vowels: {v} Consonants: {c}")
        return 0
    c += 1

    i = random.random()
    if i < 0.33:

        numRec += 1
        C()

    else:

        numRec += 1
        V()


V()