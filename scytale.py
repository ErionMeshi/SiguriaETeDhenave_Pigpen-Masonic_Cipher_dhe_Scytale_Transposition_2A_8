import math

def scytale_encrypt(text, key):
    import math

def scytale_encrypt(text, key):
    text = text.replace(" ", "")
    rows = math.ceil(len(text) / key)
    import math

def scytale_encrypt(text, key):
    text = text.replace(" ", "")
    rows = math.ceil(len(text) / key)

    grid = [''] * rows

    index = 0
    for r in range(rows):
        for c in range(key):
            if index < len(text):
                grid[r] += text[index]
                index += 1
    pass
