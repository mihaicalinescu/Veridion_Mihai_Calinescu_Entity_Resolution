def remove_duplicates(lst):
    seen = set()
    result = []

    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)

    return result

print (remove_duplicates([1, 2, 3, 2, 4, 3, 5, 1]))