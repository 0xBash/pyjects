# A plain-text.
# Number of letters to shift in the cipher.
import string


def ceaser_cipher(plain_text, shift_num):
    letters = string.ascii_lowercase
    mask = letters[shift_num:] + letters[:shift_num]
    trantab = str.maketrans(letters, mask)      # Translating Table i.e. letter-to-mask.
    print(plain_text.translate(trantab))


if __name__ == '__main__':
    words = str(input("Enter lowercase words that makes sense.\n"))
    s_value = int(input("Enter any number from 1-13:\n"))
    ceaser_cipher(words, s_value)

