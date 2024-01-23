import re

file_paths = ["cipher.txt", "text1.txt", "text2.txt"]


def removeUnwanted(content):
    reqText = re.sub("[\W_]+", "", content).upper()
    removeNumPattern = r"[0-9]"
    reqText = re.sub(removeNumPattern, "", reqText)

    return reqText


def wordCount(reqText):
    word_freq = {}
    for word in reqText:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # sorting results
    sorted_res = sorted(word_freq.items(), key=lambda x: (x[0], -x[1]))
    return sorted_res


def processFile(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        modifiedText = removeUnwanted(content)
        word_frequency = wordCount(modifiedText)

        print(f"For file: '{file_path}' - ")

        for word, freq in word_frequency:
            print(f"{word}: {freq}")

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
