import string


def shift_n(letter, amount):
    if letter not in string.ascii_lowercase:
        return letter
    new_letter = ord(letter) + amount   # ascii value: a -> 97 && z -> 122
    while new_letter > ord('z'):    # If new_letter > 122
        new_letter -= 26
    while new_letter < ord('a'):    # If new_letter < 97.
        new_letter += 26
    return chr(new_letter)      # Ascii to character


def caeser_redux(message, amount):
    enc_list = [shift_n(letter, amount) for letter in message]  # List comprehension
    print("".join(enc_list))    # enc_list to word.


if __name__ == '__main__':
    caeser_redux('hello world!', 3)
