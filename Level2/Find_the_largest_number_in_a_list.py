raw = input("Enter numbers: ")
data = raw.split()

data = [int(x) for x in data]

largest = data[0]
for x in data:
    if x > largest:
        largest = x

print(largest)
