morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

n = int(input("1 - encrypt, 2 - decrypt: "))
matn = input("Matn kiriting: ").upper()
natija = ""

if n == 1:
    for belgi in matn:
        if belgi != " ":
            natija += morse[belgi] + " "
        else:
            natija += "  "

elif n == 2:
    words = matn.split("  ")
    for word in words:
        letters = word.split()
        for kod in letters:
            for k, v in morse.items():
                if v == kod:
                    natija += k
                    break
        natija += " "

print("Natija:", natija)
