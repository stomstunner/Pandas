he = ["abc",45,89,90,10,68,90,90]
for x in he[:]:
    if x == 90:
        he.remove(90)
print(he)

# while
while 90 in he:
    he.remove(90)
print(he)

# for loop advance
he = [x for x in he if x != 90]
print(he)