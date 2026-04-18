def encrypt(text, pigpen):
    # E kthejm tekstin ne shkronja te medha
    text = text.upper()
    # Krijojm nje string bosh ku do ruajme rezultatin
    result = ""


    for char in text: #Kalojme neper çdo karakter te tekstit
        if char in pigpen:
            simboli_encpy = pigpen[char] #Nese po e shtojm simbolin perkates 
            result += simboli_encpy + " "
        else:
            result += char #nese so shkronje, e lajm qysh o

    return result #teksi i enkriptuar