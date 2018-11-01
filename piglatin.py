def piglatin(txt):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    words= txt.split(" ")
    length = len(words)
    for i in range(length):
        if words[i][0] not in vowels:
            for j in range(1,len(words[i])):
                if words[i][j] in vowels:
                    temp = words[i][j]
                    break
            for k in range(len(words[i])):
                if words[i][k] == temp:
                    break
            add1 = words[i][:k]
            add2 = words[i][k:]
            change = add2 + add1 + 'ay'
            words[i] = change
        else:
            words[i]+='yay'
    txt=" ".join(words)
    return(txt)


