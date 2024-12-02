def find(s, p):
    l = []
    n = len(p)
    for i in range(len(s)-n+1):
        if s[i:i+n] == p:
            l.append(i)
    return l

print(find("TCCGGATCCCGGGATGGA", "GG"))