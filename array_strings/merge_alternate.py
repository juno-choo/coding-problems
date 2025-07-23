def merge_alternate(word1, word2):

    result = []

    longer_word = None

    if len(word1) > len(word2):
        longer_word = len(word1)
    else:
        longer_word = len(word2)

    for i in range(longer_word):
        if i < len(word1):
            result.append(word1[i])

        if i < len(word2):
            result.append(word2[i])

    return "".join(result) 

print(merge_alternate("abc", "pqr"))
print(merge_alternate("ab", "pqrs"))
print(merge_alternate("abcd", "pq"))