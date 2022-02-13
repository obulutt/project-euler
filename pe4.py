liste = []
for i in range(100,1000):
    for j in range(100,1000):
        b = str(i*j)
        if b == b[::-1]:
            liste.append(i*j)
print(max(liste))