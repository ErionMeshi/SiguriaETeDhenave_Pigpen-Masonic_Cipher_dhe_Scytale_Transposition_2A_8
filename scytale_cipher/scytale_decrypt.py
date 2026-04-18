import math

def scytale_decrypt(ciphertext, key):
    rows = math.ceil(len(ciphertext) / key)
    cols = key

    grid = [[""] * cols for _ in range(rows)]

    index = 0
    for c in range(cols):
        for r in range(rows):
            if index < len(ciphertext):
                grid[r][c] = ciphertext[index]
                index += 1

    result = ""
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]:
                result += grid[r][c]

    return result


# test
cipher = "WECRLTEERDSOEEFEAOCAIVDEN"
key = 3

print(scytale_decrypt(cipher, key))
