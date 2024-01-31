
## Code execution
This is a python code stored in Q1.py file. Before execution make sure cipher.txt, text1.txt and text2.txt are also downloaded and the relevant or absolute paths are updated as per the system in 
file_paths = [
    "decryption/cipher.txt",
    "decryption/text1.txt",
    "decryption/text2.txt",
] 
Then run the code to see the output (obtained output at the end of this file)


## Key & Plaintext obtained
Recovery Key:
N -> A
K -> B
U -> C
C -> D
Y -> E
Z -> F
J -> G
D -> H
G -> I
I -> J
L -> K
E -> L
O -> M
A -> N
W -> O
V -> P
H -> Q
B -> R
T -> S
P -> T
X -> U
Q -> V
F -> W

Plaintext I tried to recover but doesn't seem like it worked:
TRWTPEWRVUFSEWTRWLVGQHUUVPNTSTVGBSMEVOJTRPOKUSMURSWUVONURPDUVONUWVGPOKLVASMFVIIVKWUVONBPOKUVONLRJTRWUVPUISPGPOKRSTVONLRWTRWQDPKURVCWLPOKUIHTLVPTVIPTTRWSJUTWQUFQPWNIWMSQWLWRVCWSHQFRVTMSQUSEWSMHUVQWSHTSMIQWVTRVONVGGSMHUVQWMVTOSRHQQJUVPNTRWFVQDWOTWQTRWJTRVOBWNRPEEHFRMSQTRVTVGSVMSMIQWVNTRWLVGQHUUVPNPULRVTLWFRPWMGJOWWNDWDDWQVONCPOWKVQIWUPNWUVQWCWQJKSSNPONWWNOSLPMJSHQWQWVNJSJUTWQUNWVQLWFVOIWKPOTSMWWN


## Sources:
I used two text files text1.txt and text2.txt these are the two dissertations I have worked on previously.
text1 has 14042 characters and text2 has 15777 characters


## Explanation and Working: 
In an attempt to decrypt the message,

I have followed and used a few steps in msgDecrypt.py

Step 1: converting the entire message into a standard format - 
using removeUnwanted(content):
In this function, anything other than alpabet are removed and our cipher is converted into uppercase

Step 2: Counting the characters  -
using alphabetCount(reqText):
This function iterates through the text files and counts the characters and sorts them in asecnding order of occurance as key value pairs

Step 3: Finding the key - had touble but later used the general freq for alpabet
findKey(cipher_freq, ref_freq):
This function,takes in frequencies of characters in cipher.txt and the same from ref_freq 
Initializes an empty dictionary, Assigns the character from the ciphertext to the corresponding character from the reference text.
Returns the constructed key dictionary, which represents the mapping between characters in the ciphertext and characters in the reference text based on their frequencies.

Step 4: Decryption
decrypt(ciphertext, key):
This takes in ciphertext and key, returning the decrypted plaintext.


Rest of the code calls these functions and executes them, further I have added try and catch to catch any errors and display them in the output.

## Output
For file: 'decryption/cipher.txt' - 
N: 1
K: 3
U: 4
C: 6
Y: 6
Z: 8
J: 9
D: 10
G: 10
I: 10
L: 10
E: 12
O: 15
A: 21
W: 22
V: 24
H: 25
B: 26
T: 27
P: 28
X: 28
Q: 42
F: 50
Total Characters: 397

For file: 'decryption/text1.txt' - 
Q: 9
J: 20
X: 23
Z: 24
W: 69
K: 76
B: 113
Y: 129
V: 210
P: 285
U: 352
G: 360
F: 390
H: 421
M: 448
C: 580
L: 597
D: 630
R: 826
S: 1002
O: 1075
T: 1146
A: 1153
N: 1171
I: 1222
E: 1711
Total Characters: 14042

For file: 'decryption/text2.txt' - 
Q: 5
Z: 21
J: 23
X: 42
K: 92
W: 122
B: 195
Y: 225
V: 290
G: 297
F: 333
U: 378
H: 395
D: 420
P: 430
M: 554
L: 616
C: 863
R: 1010
O: 1054
S: 1193
A: 1201
N: 1203
T: 1327
I: 1549
E: 1939
Total Characters: 15777

Recovery Key:
N -> A
K -> B
U -> C
C -> D
Y -> E
Z -> F
J -> G
D -> H
G -> I
I -> J
L -> K
E -> L
O -> M
A -> N
W -> O
V -> P
H -> Q
B -> R
T -> S
P -> T
X -> U
Q -> V
F -> W

Plaintext I tried to recover but doesn't seem like it worked:
TRWTPEWRVUFSEWTRWLVGQHUUVPNTSTVGBSMEVOJTRPOKUSMURSWUVONURPDUVONUWVGPOKLVASMFVIIVKWUVONBPOKUVONLRJTRWUVPUISPGPOKRSTVONLRWTRWQDPKURVCWLPOKUIHTLVPTVIPTTRWSJUTWQUFQPWNIWMSQWLWRVCWSHQFRVTMSQUSEWSMHUVQWSHTSMIQWVTRVONVGGSMHUVQWMVTOSRHQQJUVPNTRWFVQDWOTWQTRWJTRVOBWNRPEEHFRMSQTRVTVGSVMSMIQWVNTRWLVGQHUUVPNPULRVTLWFRPWMGJOWWNDWDDWQVONCPOWKVQIWUPNWUVQWCWQJKSSNPONWWNOSLPMJSHQWQWVNJSJUTWQUNWVQLWFVOIWKPOTSMWWN