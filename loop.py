
# new_word = ""


def reverse_string(word):
    new_word = ""

    n = len(word)
    while n > 0:
        new_ch = word[n-1]
        new_word = new_word + new_ch
        n = n-1

    return new_word


res = reverse_string("hello")
print(res)


wo = "ahmed"
print(list(reversed(wo)))
