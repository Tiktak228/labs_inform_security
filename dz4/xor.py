def read_file():
    text = ''
    with open('BohemianRhapsody.txt', 'r') as f:
        text = ''.join([line for line in f]).lower()
    return text


def write_file(encrypted_text):
    with open('./encrypted_text.txt', 'w') as f:
        f.write(encrypted_text)


def xor(text, key):
    content_codes = list(map(ord, text))
    key_codes = list(map(ord, key))
    key_codes_length = len(key_codes)
    new_codes = []
    for i in range(len(content_codes)):
        j = i % key_codes_length
        new_codes.append(content_codes[i] ^ key_codes[j])
    return ''.join(list(map(chr, new_codes)))


text = read_file()
key = input('key: ')
encrypted_text = xor(text, key)
write_file(encrypted_text)
print(text == xor(encrypted_text, key))
