w = "wwwwwwlllllllllooooooo"

r = w[0]

for ch in w:
    if ch == r[-1]:
        pass
    else:
        r = r + ch


print(r)
