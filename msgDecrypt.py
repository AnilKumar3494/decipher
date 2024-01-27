import re

file_paths = ["cipher.txt", "text1.txt", "text2.txt"]


# function to removing everhing except the alphabet and then convter to upper case
# follwoing that numbers are removed
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
            character_freq = alphabetCount(modifiedText)
            total_character_count = sum(freq for char, freq in character_freq)

            print(f"For file: '{file_path}' - ")

            for char, freq in character_freq:
                print(f"{char}: {freq}")

            print(f"Total Characters: {total_character_count}\n")

    return


# iterating through the files
for file_path in file_paths:
    processFile(file_path)
