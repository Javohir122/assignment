def classify(value):
    if value < 248:
        return "Below range"
    elif value <= 252:
        return "In range"
    else:
        return "Above range"

def calculate_average(total, count):
    return total / count

count = int(input("Enter the number of jars: "))

total = 0
below = 0
inside = 0
above = 0

for i in range(count):
    volume = int(input("Enter the jar volume: "))
    result = classify(volume)
    print(result)
    total += volume

    if result == "Below range":
        below += 1
    elif result == "In range":
        inside += 1
    else:
        above += 1
average = calculate_average(total, count)

print(f"Total volume: {total} ml")
print(f"Average volume: {average} ml")
print(f"Below range: {below}")
print(f"In range: {inside}")
print(f"Above range: {above}")