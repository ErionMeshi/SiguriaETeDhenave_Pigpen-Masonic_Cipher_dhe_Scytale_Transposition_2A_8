import math

def columnar_transposition_enkriptim(text, key):
    text = text.replace(" ", "")
    cols = len(key)
    rows = math.ceil(len(text) / cols)

    grid = ['' for _ in range(cols)]

    for i, char in enumerate(text):
     grid[i % cols] += char
    
    
    sorted_key = sorted(list(enumerate(key)), key=lambda x: x[1])
    
    ciphertext = ''
    for index, _ in sorted_key:
        ciphertext += grid[index]

    return ciphertext