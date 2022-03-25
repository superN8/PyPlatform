lines = open("words2.txt", "r")

alphabet = [('a', 0), ('b', 2), ('c', 1), ('d', 0), ('e', 0), ('f', 0), ('g', 0), ('h', 0), ('i', 0),
            ('j', 0), ('k', 0), ('l', 0), ('m', 0), ('n', 0), ('o', 0), ('p', 0), ('q', 0), ('r', 0),
            ('s', 0), ('t', 0), ('u', 0), ('v', 0), ('w', 0), ('x', 0), ('y', 0), ('z', 0)]


def freq(e):
    return e[1]


for word in lines:
    for c in word:
        for i in range(0, len(alphabet)):
            if c == alphabet[i][0]:
                alphabet[i] = (alphabet[i][0], alphabet[i][1] + 1)
                break

alphabet.sort(reverse=True, key=freq)
alphaStr = ""
for t in alphabet:
    alphaStr += t[0]
print(alphabet)
print(alphaStr)
