import re


def removeUnwanted(content):
    reqText = re.sub("[^a-zA-Z]", "", content).upper()
    removeNumPattern = r"[0-9]"
    reqText = re.sub(removeNumPattern, "", reqText)
    return reqText


def alphabetCount(reqText):
    character_freq = {}
    for char in reqText:
        if char in character_freq:
            character_freq[char] += 1
        else:
            character_freq[char] = 1
    sorted_res = sorted(character_freq.items(), key=lambda x: (x[1], x[0]))
    return sorted_res


def findKey(cipher_freq, ref_freq):
    key = {}
    for cipher_char, _ in cipher_freq:
        ref_char, _ = ref_freq.pop(0)
        key[cipher_char] = ref_char
    return key


def decrypt(ciphertext, key):
    return "".join(key.get(char, char) for char in ciphertext)


file_paths = [
    "decryption/cipher.txt",
    "decryption/text1.txt",
    "decryption/text2.txt",
]

# Dictionary to store the character frequencies for reference
ref_freq_dict = {}

try:
    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            modifiedText = removeUnwanted(content)
            character_freq = alphabetCount(modifiedText)

            total_character_count = sum(freq for char, freq in character_freq)

            print(f"For file: '{file_path}' - ")
            for char, freq in character_freq:
                print(f"{char}: {freq}")

            print(f"Total Characters: {total_character_count}\n")

            if file_path == "decryption/cipher.txt":
                # Store the character frequencies for the ciphertext for later use
                ref_freq_dict[file_path] = character_freq

    # reference frequencies for alpabet
    ref_freq_dict["decryption/text1.txt"] = alphabetCount("ETAOINSHRDLCUMWFGYPBVKJXQZ")

    # Find the key to decrypt the ciphertext
    cipher_freq = ref_freq_dict["decryption/cipher.txt"]
    ref_freq = ref_freq_dict["decryption/text1.txt"]
    key = findKey(cipher_freq, ref_freq)

    print("Recovery Key:")
    for cipher_char, plain_char in key.items():
        print(f"{cipher_char} -> {plain_char}")

    # Decrypt the ciphertext using the key
    ciphertext_path = "decryption/cipher.txt"
    with open(ciphertext_path, "r", encoding="utf-8") as cipher_file:
        ciphertext = removeUnwanted(cipher_file.read())
        plaintext = decrypt(ciphertext, key)

    print("\nRecovered Plaintext:")
    print(plaintext)

except FileNotFoundError as e:
    print(f"Error: {e}. Check the file paths.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
