def cleanword(word):
    if len(word) == 1:
        return word
    elif word[0] == word[1]:
        return cleanword(word[1:])
    else:
        return word[0] + cleanword(word[1:])


print(cleanword("wwwwwwwwwwooooooorrrrrrrrlllllllllddddd"))
# very important 63
print("-"*50)

while input("a=") is str:
    try:
        a = float(a)
    except:
        a = input("a====")
else:
    a = input("a")
