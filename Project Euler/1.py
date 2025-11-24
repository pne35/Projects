ls = []
t = 0

for count in range(1000):
    if count % 3 == 0:
        ls.append(count)
        t += count 

    elif count % 5 == 0:
        ls.append(count)
        t += count 

print(ls)
print(t)