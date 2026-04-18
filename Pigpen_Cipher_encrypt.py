def encrypt(text, pigpen):
    text = text.upper()
    result = ""

    for char in text:
        if char in pigpen:
            result += pigpen[char] + " "
        else:
            result += char

    return result