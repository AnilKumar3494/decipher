import re

file_paths = ["cipher.txt", "text1.txt", "text2.txt"]


# function to removing everhing except the alphabet and then convter to upper case
# follwoing that numbers are removed
def removeUnwanted(content):
    reqText = re.sub("[\W_]+", "", content).upper()
    removeNumPattern = r"[0-9]"
    reqText = re.sub(removeNumPattern, "", reqText)

    return reqText


# function for counting the characters
def aplhabetCount(reqText):
    character_freq = {}
    for char in reqText:
        if char in character_freq:
            character_freq[char] += 1
        else:
            character_freq[char] = 1

    # sorting results as alphabet and repetition pair
    sorted_res = sorted(character_freq.items(), key=lambda x: (x[0], -x[1]))
    return sorted_res


def processFile(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        modifiedText = removeUnwanted(content)

        if file_path != "cipher.txt":
            character_freq = aplhabetCount(modifiedText)
            print(f"For file: '{file_path}' - ")

            for char, freq in character_freq:
                print(f"{char}: {freq}")

            print()
        else:
            print(f"For file: '{file_path}' - ")
            print(f"Decrypted content:")

            text1_freq = aplhabetCount(
                removeUnwanted(open("text1.txt", "r", encoding="utf-8").read())
            )
            text2_freq = aplhabetCount(
                removeUnwanted(open("text2.txt", "r", encoding="utf-8").read())
            )

            cipher_mapping = {}

            for (cipher_char, _), (text1_char, _) in zip(
                aplhabetCount(modifiedText), text1_freq
            ):
                cipher_mapping[cipher_char] = text1_char

            for (cipher_char, _), (text2_char, _) in zip(
                aplhabetCount(modifiedText), text2_freq
            ):
                cipher_mapping[cipher_char] = text2_char

            decrypted_text = "".join(
                cipher_mapping.get(char, char) for char in modifiedText
            )
            print(decrypted_text)

            print()

    return


# iterating through the files
for file_path in file_paths:
    processFile(file_path)


# ## word_file_path = file_paths[2]
# def textFromWordDoc(word_file_path):
#     try:
#         doc = Document(word_file_path)

#         for para in doc.paras:
#             print(para.text)
#     except Exception as e:
#         print(f"Cannot read the Word file '{word_file_path}: {e}")


# textFromWordDoc(word_file_path)


# OBFOSVFBPUWQVFOBFEPJHDUUPSAOQOPJKQNVPTIOBSTLUQNUBQFUPTAUBSCUPTAUFPJSTLEPMQNWPGGPLFUPTAKSTLUPTAEBIOBFUPSUGQSJSTLBQOPTAEBFOBFHCSLUBPRFESTLUGDOEPSOPGSOOBFQIUOFHUWHSFAGFNQHFEFBPRFQDHWBPONQHUQVFQNDUPHFQDOQNGHFPOBPTAPJJQNDUPHFNPOTQBDHHIUPSAOBFWPHCFTOFHOBFIOBPTKFABSVVDWBNQHOBPOPJQPNQNGHFPAOBFEPJHDUUPSASUEBPOEFWBSFNJITFFACFCCFHPTARSTFLPHGFUSAFUPHFRFHILQQASTAFFATQESNIQDHFHFPAIQIUOFHUAFPHEFWPTGFLSTOQNFFA
