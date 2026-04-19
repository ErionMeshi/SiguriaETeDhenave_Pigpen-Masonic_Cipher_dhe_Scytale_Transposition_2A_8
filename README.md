# SiguriaETeDhenave_Pigpen/Masonic_Cipher_dhe_Scytale_Transposition_2A_8

# 🔐 Pigpen & Scytale Cipher Implementation

Ky projekt implementon dy algoritme të enkriptimit dhe dekriptimit:
- Pigpen Cipher (substitution cipher)
- Scytale Cipher (transposition cipher)

---------------------------------------------------------------------------------------------------------------

# ▶️ Si të ekzekutohet programi

## Kërkesat
- Python 3 i instaluar

## Ekzekutimi
1. Hap terminalin në folderin e projektit
2. Ekzekuto komandën:

--bash
python cipher.py
---------------------------------------------------------------------------------------------------------------
🔐 Pigpen Cipher
Përshkrimi

Pigpen Cipher është një algoritëm zëvendësimi ku çdo shkronjë e alfabetit zëvendësohet me një simbol grafik. Rendi i shkronjave nuk ndryshon, vetëm forma e tyre.

Funksionimi
Teksti konvertohet në shkronja të mëdha
Çdo shkronjë zëvendësohet me simbol nga dictionary
Dekriptimi bëhet duke përdorur mapping të kundërt

Shembull
Enkriptim:
encrypt("HELLO", pigpen)

Output:
┴ ┼ ⌞ ⌞ ⊢


Dekriptim:
decrypt("┴ ┼ ⌞ ⌞ ⊢", pigpen)

Output:
HELLO
---------------------------------------------------------------------------------------------------------------
🔁 Scytale Cipher
Përshkrimi

Scytale Cipher është algoritëm transpozimi ku shkronjat nuk ndryshohen, por riorganizohen në një tabelë me rreshta dhe kolona.

Funksionimi
-Teksti vendoset në matricë sipas një key (numër kolonash)
-Leximi bëhet kolonë për kolonë për enkriptim
-Dekriptimi rikthen rendin origjinal

Shembull
Enkriptim:
scytale_encrypt("HELLO WORLD", 3)

Output:
HORELLOLXWXD

Dekriptim:
scytale_decrypt("HORELLOLXWXD", 3)

Output:
HELLOWORLD

👨‍💻 Autor
Erion Meshi
Zymer Ahmetaj
Erion Qerimi
Erijon Elshani

