def replace_value(values, index, new_value):
    values[index] = new_value
    return None
    
def find_first(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1
    
def summarize(values):
    return min(values), max(values), sum(values)

if __name__ == "__main__":
    days = int(input("Enter the number of days: "))
    original = []
    for day in range(days):
        emails = int(input("Enter the number of emails received: "))
        original.append(emails)

    updated = original[:]
    index = int(input("Enter the index to correct: "))
    new_value = int(input("Enter the new number of emails: "))
    replace_value(updated, index, new_value)

    target = int(input("Enter the number of emails to search for: "))
    first_index = find_first(updated, target)
    matching_count = updated.count(target)
    minimum, maximum, total = summarize(updated)
    sorted_values = sorted(updated)

    print(f"Original: {original}")
    print(f"Updated: {updated}")
    print(f"Sorted: {sorted_values}")
    print(f"Minimum number of emails: {minimum}")
    print(f"Maximum number of emails: {maximum}")
    print(f"Total number of emails: {total}")
    if first_index == -1:
        print(f"Target not found")
    else:
        print(f"First matching index: {first_index}")
    print(f"Matching values: {matching_count}")
