# show details of the inputs entered in sorted order

# give me an empty listx
names = []

for _ in range(3):
    # name = input("wheta syour name? ")
    # print(f"hello, {name}")
    # names.append
    names.append(input("wheta syour name? "))

for name in sorted(names):
    print(f"hello, {name}")