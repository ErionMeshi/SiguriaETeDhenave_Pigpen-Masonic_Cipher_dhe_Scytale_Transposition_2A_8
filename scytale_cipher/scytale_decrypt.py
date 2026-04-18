def scytale_decrypt(ciphertext, key):
    plaintext = [''] * key

    col_length = len(ciphertext) // key
    extra = len(ciphertext) % key

    index = 0

    for i in range(key):
        length = col_length + (1 if i < extra else 0)
        plaintext[i] = ciphertext[index:index + length]
        index += length

    result = ""
    for i in range(col_length + 1):
        for j in range(key):
            if i < len(plaintext[j]):
                result += plaintext[j][i]

    return result


# test
cipher = "WECRLTEERDSOEEFEAOCAIVDEN"
key = 3

print(scytale_decrypt(cipher, key))
