import numbers


def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output

listofNumbers = [1,2,3,5,6,7,8,9,11,12,13,14,15,17,18,19,20]
print(findMissingNumbers(listofNumbers))