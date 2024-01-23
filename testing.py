import string
from collections import Counter


def decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            decrypted_text += key[char]
        else:
            decrypted_text += char
    return decrypted_text


def frequency_analysis(text):
    text = text.upper()
    letter_count = Counter(char for char in text if char.isalpha())
    total_letters = sum(letter_count.values())
    frequencies = {char: count / total_letters for char, count in letter_count.items()}
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    return [char for char, _ in sorted_frequencies]


# Ciphertext
ciphertext = (
    "PBFPVYFBQXZTYFPBFEQJHDXXQVAPTPQJKTOYQWIPBVWLXTOXBTFXQWA"
    "XBVCXQWAXFQJVWLEQNTOZQGGQLFXQWAKVWLXQWAEBIPBFXQVXGTVJV"
    "WLBTPQWAEBFPBFHCVLXBQUFEVWLXGDPEQVPQGVPPBFTIXPFHXZHVFAG"
    "FOTHFEFBQUFTDHZBQPOTHXTYFTODXQHFTDPTOGHFQPBQWAQJJTODXQH"
    "FOQPWTBDHHIXQVAPBFZQHCFWPFHPBFIPBQWKFABVYYDZBOTHPBQPQJT"
    "QOTOGHFQAPBFEQJHDXXQVAVXEBQPEFZBVFOJIWFFACFCCFHQWAUVWFL"
    "QHGFXVAFXQHFUFHILTTAVWAFFAWTEVOITDHFHFQAITIXPFHXAFQHEFZ"
    "QWGFLVWPTOFFA"
)

# English alphabet frequency analysis
english_frequency = frequency_analysis(string.ascii_uppercase)

# Ciphertext frequency analysis
ciphertext_frequency = frequency_analysis(ciphertext)

# Create a mapping between the most frequent letters in the ciphertext and the English alphabet
key = dict(zip(ciphertext_frequency, english_frequency))

# Decrypt the ciphertext
decrypted_text = decrypt(ciphertext, key)

# Print results
print("Ciphertext Frequency Analysis:", ciphertext_frequency)
print("English Alphabet Frequency Analysis:", english_frequency)
print("Key:", key)
print("Decrypted Text:", decrypted_text)
