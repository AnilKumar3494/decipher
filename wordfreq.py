import re

file_paths = ['cipher.txt', 'text1.txt']

def removeUnwanted(content):
    removeNumPattern = r'[0-9]'
    reqText = re.sub('[\W_]+', '', content).upper()
    reqText = re.sub(removeNumPattern, '', reqText)
    
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
    with open (file_path, 'r') as file:
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

