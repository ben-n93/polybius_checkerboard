import string

def create_polybius_checkerboard():
    """Create a dictionry representing a polybius checkerboard/square."""
    polybius_checkerboard = {}
    column = 1
    row = 1
    for character in string.ascii_lowercase:
        if character == "i":
            polybius_checkerboard[character] = 24
            column = 4
        else:
            polybius_checkerboard[character] = str(row) + str(column)
            column += 1
            if column == 6:
                column = 1
                row += 1
    return polybius_checkerboard


def encrypt(plaintext):
    """Encrypt a plaintext message using the polybius checkerboard cipher."""
    plaintext = plaintext.lower()
    polybius_checkerboard = create_polybius_checkerboard()
    ciphertext = []
    for character in plaintext:
        coordinate = polybius_checkerboard.get(character)
        if coordinate is None:
            ciphertext.append(character)
        else:
            ciphertext.append(str(coordinate))
    ciphertext = " ".join(ciphertext)
    return ciphertext


def decrypt(ciphertext):
    """Decrypt a ciphertext using the polybius checkerboard cipher."""
    polybius_checkerboard = create_polybius_checkerboard()
    plaintext = []
    keys = list(polybius_checkerboard.keys())
    values = list(polybius_checkerboard.values())
    ciphertext = ciphertext.split(" ")
    for character in ciphertext:
        try:
            index = values.index(character)
            plaintext_letter = keys[index]
            plaintext.append(plaintext_letter)
        except ValueError:
            plaintext.append(character)
    plaintext = "".join(plaintext)
    return plaintext
