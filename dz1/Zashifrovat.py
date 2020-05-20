def Caesar(tekst):
    sourceText = tekst
    sourceText = sourceText.lower()
    a = 3
    alphabet = "абвгдежзиклмнопрстуфхцчшщыьэюяабвгдежзиклмнопрстуфхцчшщыьэюя"
    result = ""
    for letter in sourceText:
        position = alphabet.find(letter)
        newPosition = position + a
        if letter in alphabet:
            result = result + alphabet[newPosition]
        else:
            result = result + letter
    return result

b = open('Vorovaiki.txt', 'r')
text = "".join(b)
c = Caesar(text)
d = open('VorovaikiEnd.txt', 'w')
d.writelines(c)
d.close()
