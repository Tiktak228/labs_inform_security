def MamaOoo():
    text = ''
    with open('BohemianRhapsody.txt', 'r') as f:
        text = ''.join([line for line in f]).lower()
    return text


def IDontWantToDie (encrypted):
    with open('BohemianRhapsodyEnd.txt', 'w') as f:
        f.write(encrypted)


def xor(text, key):
    content_codes = list(map(ord, text))
    key_codes = list(map(ord, key))
    key_codes_length = len(key_codes)
    new_codes = []
    for i in range(len(content_codes)):
        j = i % key_codes_length
        new_codes.append(content_codes[i] ^ key_codes[j])
    return ''.join(list(map(chr, new_codes)))


text = MamaOoo()
key = input('key: ')
encrypted = xor(text, key)
IDontWantToDie (encrypted)
print(text == xor(encrypted, key))
