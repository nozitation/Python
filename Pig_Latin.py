def E_to_pl ():
    st = input()
    st = st.split()
    i = 0
    for x in st:
        x = list(x)
        a = x[0]
        x.remove(x[0])
        x.append(a)
        x.append('ay')
        x = ''.join(x)
        st[i] = x
        i += 1
    st = " ".join(st)
    print(st)
    return st

E_to_pl ()