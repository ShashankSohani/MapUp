# reverse list by nth element

def reverse(list, n):

    result = []

    i = 0

    while i< len(list):

        if i +n <= len(list):
            group = list[i: i+n]
        
        else:
            group  = list[i:]

        group.reverse()
        result.extend(group)
        i+=n

    return result

print(reverse([1, 2, 3, 4, 5, 6, 7, 8], 3))
print(reverse([1, 2, 3, 4, 5], 2))
print(reverse([10, 20, 30, 40, 50, 60, 70], 4))