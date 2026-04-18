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

    result = ""
    for c in range(key):
        for r in range(rows):
            if c < len(grid[r]):
                result += grid[r][c]

    return result
    pass
