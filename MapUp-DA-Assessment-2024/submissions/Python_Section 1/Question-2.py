# list and dict


def group(strings):

    groups = {}

    for string in strings:
        length = len(string)

        if length not in groups:
            groups[length] = []

        groups[length].append(string)
    return dict(sorted(groups.items()))

print(group(["apple", "bat", "car", "elephant", "dog", "bear"]))
print(group(["one", "two", "three", "four"]))