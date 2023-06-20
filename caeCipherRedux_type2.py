import string


def shift_n(letter, table):
    try:
        index = string.ascii_lowercase.index(letter)    # Passing indices to the alphas from a-z.
        return table[index]     # Returning the indices table.
    except ValueError:
        return letter   # In case of exception: Letters rather than lowercase.


def caesar(message, amount):
    amount = amount % 26    # Amount value stays between 0-25
    table = string.ascii_lowercase[amount:] + string.ascii_lowercase[:amount]   # Lowercase alphas shifts by amount.
    enc_list = [shift_n(letter, table) for letter in message]   # List comprehension.
    print("".join(enc_list))    # All letters in the list joined together to form a encrypted word.


if __name__ == '__main__':
    caesar('hollow world!', 3)     # Passing message and amount to the caeser().
