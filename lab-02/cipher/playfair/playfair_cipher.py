class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        key_set = []
        for char in key:
            if char not in key_set and char.isalpha():
                key_set.append(char)

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            if letter not in key_set:
                key_set.append(letter)

        matrix = [key_set[i:i+5] for i in range(0, 25, 5)]
        return matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None, None

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.replace("J", "I").upper()
        prepared_text = ""
        i = 0

        while i < len(plain_text):
            a = plain_text[i]
            b = plain_text[i+1] if i+1 < len(plain_text) else "X"

            if a == b:
                prepared_text += a + "X"
                i += 1
            else:
                prepared_text += a + b
                i += 2
        if len(prepared_text) % 2 != 0:
            prepared_text += "X"

        encrypted_text = ""
        for i in range(0, len(prepared_text), 2):
            a, b = prepared_text[i], prepared_text[i+1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2]
                encrypted_text += matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            a, b = cipher_text[i], cipher_text[i+1]
            row1, col1 = self.find_letter_coords(matrix, a)
            row2, col2 = self.find_letter_coords(matrix, b)

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1]
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2]
                decrypted_text += matrix[row2][col1]

        plain_text = ""
        i = 0
        while i < len(decrypted_text):
            a = decrypted_text[i]
            b = decrypted_text[i+1] if i+1 < len(decrypted_text) else ""

            if b == "X" and i+2 < len(decrypted_text) and decrypted_text[i] == decrypted_text[i+2]:
                plain_text += a
                i += 1
            else:
                plain_text += a + b
                i += 2

        return plain_text
