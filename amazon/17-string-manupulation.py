#!/bin/python3

import sys

def getRemovableIndices(str1, str2):
    n = len(str1)
    m = len(str2)

    # str1 must be exactly one char longer
    if n != m + 1:
        return [-1]

    i = j = 0

    # Find first mismatch
    while i < n and j < m and str1[i] == str2[j]:
        i += 1
        j += 1

    remove_idx = i

    # Skip one character in str1
    i += 1

    # Verify remaining characters match
    while i < n and j < m:
        if str1[i] != str2[j]:
            return [-1]
        i += 1
        j += 1

    result = [remove_idx]

    # Include identical adjacent chars before remove_idx
    k = remove_idx - 1
    while k >= 0 and str1[k] == str1[remove_idx]:
        result.append(k)
        k -= 1

    return sorted(result)


if __name__ == '__main__':
    str1 = input().strip()
    str2 = input().strip()

    result = getRemovableIndices(str1, str2)

    print('\n'.join(map(str, result)))