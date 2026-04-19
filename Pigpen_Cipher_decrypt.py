def decrypt(cipher_text, pigpen):
    reverse_pigpen = {value: key for key, value in pigpen.items()}
    
    result = ""
    
    #Simbolet janë ndarë me hapësirë, prandaj përdorim split()
    symbols = cipher_text.split()
    
    for sym in symbols: #Kalojme neper çdo karakter te tekstit
        if sym in reverse_pigpen:
            result += reverse_pigpen[sym]
        else:
            result += sym  # në rast se ka karaktere të tjera
    
    return result #Teksti i dekriptuar

pigpen = {
    'A':'┌','B':'┬','C':'┐','D':'├','E':'┼','F':'┤','G':'└','H':'┴','I':'┘',
    'J':'⌜','K':'⌝','L':'⌞','M':'⌟','N':'⊣','O':'⊢','P':'⊥','Q':'∧','R':'∨',
    'S':'□','T':'■','U':'▢','V':'▣','W':'◇','X':'◆','Y':'○','Z':'●'
}

print(decrypt("┴ ┼ ⌞ ⌞ ⊢", pigpen))  # Output: "HELLO"