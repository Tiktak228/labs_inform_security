def Caesar(tekst):
    sourceText = tekst
    sourceText = sourceText.lower()
    a = 3
    alphabet = "яюэьыщшчцхфутсрпонмлкизжедгвбаяюэьыщшчцхфутсрпонмлкизжедгвба"
    result = ""
    for letter in sourceText:
        position = alphabet.find(letter)
        newPosition = position + a
        if letter in alphabet:
            result = result + alphabet[newPosition]
        else:
            result = result + letter
    return result

b = open('VorovaikiEnd.txt', 'r')
text = "".join(b)
c = Caesar(text)
d = open('VorovaikiEndP.txt', 'w')
d.writelines(c)
d.close()
