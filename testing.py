import re
from collections import Counter

file_paths = ["cipher.txt", "text1.txt", "text2.txt"]


def removeUnwanted(content):
    reqText = re.sub("[^a-zA-Z]", "", content).upper()
    removeNumPattern = r"[0-9]"
    reqText = re.sub(removeNumPattern, "", reqText)
    return reqText


def alphabetCount(reqText):
    character_freq = Counter(reqText)
    sorted_res = sorted(character_freq.items(), key=lambda x: (x[1], x[0]))
    return sorted_res


def replaceCharacters(cipher_text, text1, text2):
    text = removeUnwanted(text1 + text2)
    text_freq = Counter(text)

    replaced_text = ""
    for char in cipher_text:
        if char.isalpha():
            least_freq_char = min(text_freq, key=text_freq.get)
            replaced_text += least_freq_char
            text_freq[least_freq_char] += 1
        else:
            replaced_text += char

    return replaced_text


def processFile(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        modifiedText = removeUnwanted(content)

        if file_path != "cipher.txt":
            character_freq = alphabetCount(modifiedText)
            total_character_count = sum(freq for char, freq in character_freq)

            print(f"For file: '{file_path}' - ")

            for char, freq in character_freq:
                print(f"{char}: {freq}")

            print(f"Total Characters: {total_character_count}\n")

        else:
            character_freq = alphabetCount(modifiedText)
            total_character_count = sum(freq for char, freq in character_freq)

            print(f"For file: '{file_path}' - ")

            for char, freq in character_freq:
                print(f"{char}: {freq}")

            print(f"Total Characters: {total_character_count}\n")

            # Replace characters in 'cipher.txt'
            decrypted_msg = replaceCharacters(
                modifiedText,
                open("text1.txt", encoding="utf-8").read(),
                open("text2.txt", encoding="utf-8").read(),
            )
            print(f"Decrypted Message: {decrypted_msg}\n")

    return


for file_path in file_paths:
    processFile(file_path)
