import random


class Polyb:
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    def __init__(self, file):
        self.file = file
        self.key = self.RandomKey()
        self.cont = self.encrypted_text = self.DecryptedText = None

    def ReadText(self):
        alphabet = Polyb.alphabet
        with open(self.file, 'r', encoding='utf8') as f:
            self.cont = ''.join([line for line in f]).upper()
        self.cont = list(self.cont)
        for i in range(len(self.cont)):
            if self.cont[i] == 'J':
                self.cont[i] = 'I'
        self.cont = list(filter(lambda s: s in alphabet + ' ', ''.join(self.cont)))
        self.cont = ''.join(self.cont)

    def RandomKey(self):
        alphabet = Polyb.alphabet
        alphabet_indexes = list(range(len(alphabet)))
        random.shuffle(alphabet_indexes)
        key = ''.join([alphabet[i] for i in alphabet_indexes])
        key = [list(key[i:i+5]) for i in range(0, len(key), 5)]
        with open('./keyFile.txt', 'w', encoding='utf8') as f:
            for i in range(len(key)):
                for j in range(len(key[i])):
                    f.write(f'{key[i][j]} - {i}, {j}\n')
        return key

    def coordinates(self, word):
        coordinates = []
        for i in list(word):
            for row in range(len(self.key)):
                if i in self.key[row]:
                    column = self.key[row].index(i)
                    coordinates.append([row, column])
        return coordinates

    def EncryptWord(self, word):
        coordinates = self.coordinates(word)
        coordinates = [*[i[0] for i in coordinates], *[i[1] for i in coordinates]]
        coordinates = [[coordinates[i], coordinates[i+1]] for i in range(0, len(coordinates), 2)]
        return ''.join([self.key[i][j] for i, j in coordinates])

    def DecryptWord(self, word):
        coordinates = self.coordinates(word)
        coordinates = ' '.join([' '.join([str(j) for j in i]) for i in coordinates])
        coordinates = list(map(int, coordinates.split()))
        half_length = len(coordinates) // 2
        coordinates = list(zip(coordinates[:half_length], coordinates[half_length:]))
        return ''.join([self.key[i][j] for i, j in coordinates])

    def encrypt_text(self):
        self.encrypted_text = ' '.join([self.EncryptWord(i) for i in self.cont.split()])

    def decrypt_text(self):
        self.decrypted_text = ' '.join([self.DecryptWord(i) for i in self.encrypted_text.split()])
        print(self.decrypted_text == self.cont)

    def write_file(self):
        with open('./PumpedUpKicksEnd.txt', 'w', encoding='utf8') as f:
            f.write(self.encrypted_text)


polybia = Polyb('./PumpedUpKicks.txt')
polybia .ReadText()
polybia .encrypt_text()
polybia .decrypt_text()
polybia .write_file()
