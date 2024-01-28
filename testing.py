import re

file_paths = ["cipher.txt", "text1.txt", "text2.txt"]


# function to removing everything except the alphabet and then convert to upper case
# following that numbers are removed
def removeUnwanted(content):
    reqText = re.sub("[^a-zA-Z]", "", content).upper()
    removeNumPattern = r"[0-9]"
    reqText = re.sub(removeNumPattern, "", reqText)
    return reqText


# function for counting the characters
def alphabetCount(reqText):
    character_freq = {}
    for char in reqText:
        if char in character_freq:
            character_freq[char] += 1
        else:
            character_freq[char] = 1
    # sorting results as alphabet and repetition pair
    sorted_res = sorted(character_freq.items(), key=lambda x: (x[1], x[0]))
    return sorted_res


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

        else:  # Handle the case for cipher.txt
            # Combine the texts from text1.txt and text2.txt
            combined_text = ""
            for other_file_path in file_paths[1:]:
                with open(other_file_path, "r", encoding="utf-8") as other_file:
                    combined_text += removeUnwanted(other_file.read())

            # Count the characters in the combined text
            combined_character_freq = alphabetCount(combined_text)

            print(f"For file: '{file_path}' - ")

            for char, freq in combined_character_freq:
                print(f"{char}: {freq}")

            print(
                f"Total Characters: {sum(freq for char, freq in combined_character_freq)}\n"
            )

            # Replace characters in cipher.txt based on the least frequent characters in combined_text
            replacement_dict = {char: freq[0] for char, freq in combined_character_freq}
            decrypted_msg = "".join(
                replacement_dict.get(char, char) for char in modifiedText
            )

            print(f"Decrypted Message: {decrypted_msg}\n")

    return


# iterating through the files
for file_path in file_paths:
    processFile(file_path)
