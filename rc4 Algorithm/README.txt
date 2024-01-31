RC4 - Rivest Cipher 4 is a form of stream cipher that encrypts messages one byte at a time.

## Working of RC4
The user inputs a plain text file and a secret key. 
The encryption algorithm then generates the keystream.
This keystream is now XOR ed with the plain text, this XORing is done byte by byte to produce the encrypted text.


## Executing the code
If on a local system make sure to have gcc - for c programming
Copy the entire code in Q2.c and paste in the IDE or Compiler and run the code.
(or)
Alternatively, we can use any online compiler to paste and run the code in Q2.c


## Implementing the Algorithm & Working

# Functions in my C code:
void swapping()
This function is used to swap the characters

rc4_initialization()
This function sets the permutation array with 0 to 255 bits
And then sets the Key Scheduing Algorithm used for shuffling

rc4_keystream_generation()
Function to Generation of single byte keystream and swapping elements in the permutaion array

And then in the 

main()
Key length is defined and the Initialization phase are executed

## The a,b,c parts of the implementation are 
    
    (a)
    printf("a. Permutation S after initialization:\n");
    for (int row = 0; row < 16; row++) {
        for (int col = 0; col < 16; col++) {
            printf("%02X ", S[row * 16 + col]);
        }
        printf("\n");
    }
    printf("i = %d, j = %d\n\n", i, j);


    (b)
    printf("b. Permutation S after generating the first 100 bytes of keystream:\n");
    for (int k = 0; k < 100; k++) {
        rc4_keystream_generation(S, &i, &j);
    }
    for (int row = 0; row < 16; row++) {
        for (int col = 0; col < 16; col++) {
            printf("%02X ", S[row * 16 + col]);
        }
        printf("\n");
    }
    printf("i = %d, j = %d\n\n", i, j);

    (c)
    printf("c. Permutation S after generating the first 1000 bytes of keystream:\n");
    for (int k = 0; k < 1000; k++) {
        rc4_keystream_generation(S, &i, &j);
    }
    for (int row = 0; row < 16; row++) {
        for (int col = 0; col < 16; col++) {
            printf("%02X ", S[row * 16 + col]);
        }
        printf("\n");
    }
    printf("i = %d, j = %d\n", i, j);


## Output

a. Permutation S after initialization:
4C 46 51 0E 36 AA 27 24 14 00 70 80 42 7F A7 A9 
8E 94 0C 7D 7B 37 78 BE AF 09 C0 9B E2 0D 3C 6C 
04 ED 1F B8 A2 68 DB 3F D6 76 BA BC C2 D5 3B FF 
39 2E 4E BD FA 18 B2 B1 86 6B FC 1E 73 5B 75 35 
1A 13 D7 AD 74 66 F7 B3 AC FB 07 AB E3 41 77 57 
53 84 98 E8 DD 31 11 A1 D2 16 82 72 F9 6A 40 33 
8C C4 99 02 CF 81 DC 5E 9C 5A B4 22 C1 5F CC 0B 
56 30 C7 7C 7A 9A 10 CD 4D 83 65 7E EE CE 71 34 
C8 62 FD 49 F4 9F BF 2A 8F 6D 1C 0A C9 EF E4 B9 
06 D8 3D 3A BB A8 B5 A4 C3 43 52 4B A0 05 A5 93 
90 AE 48 D4 A6 2D 6F A3 63 E1 8A 8D B0 5D B6 23 
EA 60 44 69 92 17 2F 0F 50 2B F5 F6 32 B7 29 01 
45 12 59 26 D3 C6 87 D9 E5 DE 47 5C 6E CB 1D 58 
08 4F EB DA 55 89 85 F0 E6 E7 F1 C5 03 F8 D0 38 
D1 FE E0 67 88 9D 25 CA EC 8B 19 21 15 28 F3 97 
79 20 DF 91 61 4A 54 1B E9 9E 3E F2 64 2C 96 95 
i = 0, j = 0

b. Permutation S after generating the first 100 bytes of keystream:
4C F7 A4 2D C5 41 C4 3F 88 14 F9 55 70 BA 73 4E 
7C 3B 1A 42 AD 4F 6C 37 C8 6D FB 0C 87 DA 9D 04 
D5 66 BC 67 AA 28 98 94 F8 E8 A8 C2 AB 00 FC 82 
3A 12 6B 6E E2 D0 06 13 D9 3C 72 E3 91 31 26 E9 
7D 75 5B B3 F6 78 5E 52 45 AF 2A 6F D3 9F 11 0F 
DD E4 E5 A0 ED 77 8C 97 2E F0 85 08 53 7A 92 CA 
7B B0 93 AE 56 81 DC 46 9C 5A B4 22 C1 5F CC 0B 
CF 30 C7 8E 6A 9A 10 CD 4D 83 65 7E EE CE 71 34 
C0 62 FD 49 F4 A2 BF 07 8F 09 1C 0A C9 EF 84 B9 
B2 D8 3D 39 BB 7F B5 51 C3 43 D7 4B 76 05 A5 99 
90 02 48 D4 A6 0E 1F A3 63 E1 8A 8D 27 5D B6 23 
EA 60 44 69 40 17 2F 57 50 2B F5 74 32 B7 29 01 
AC D2 59 B1 1E C6 FA 86 DB DE 47 5C BD CB 1D 58 
24 BE EB 0D 80 89 FF 16 E6 E7 F1 36 03 D6 18 38 
D1 FE E0 B8 9B A9 25 33 EC 8B 19 21 15 68 F3 A1 
79 20 DF A7 61 4A 54 1B 35 9E 3E F2 64 2C 96 95 
i = 100, j = 112

c. Permutation S after generating the first 1000 bytes of keystream:
64 ED 3C 12 A7 7E F0 A0 57 5A A9 1D 91 F1 F8 11 
00 5B C0 9B DD 6F 89 21 13 F6 16 DF D0 9D 67 D7 
33 8E 63 E7 65 02 FD 78 7A 95 D8 38 E0 F7 46 2A 
29 A6 C4 AE 2C 56 B6 93 34 53 42 9F 0B 35 C6 FA 
52 DE 7D 43 92 5E A8 68 CE CB 99 F5 A3 86 8D C3 
54 48 E1 79 2F 55 60 26 D4 5D 74 72 10 9E 69 39 
D9 3F BC 0F B3 96 2B EE 22 E6 D5 94 03 6E 62 EB 
80 7B 20 4D 3E 8F 6B 44 FE 77 E9 14 2E 0C 1F 75 
84 41 59 98 5F 4B 47 F9 CD AD 3D 01 31 B1 3B 36 
DB C8 5C 7F 7C 1E CC 50 4F 0D 8B A4 B2 37 E5 F2 
19 87 BD B8 27 4C C9 88 07 F4 18 90 85 C2 9C CF 
E4 61 1C B7 49 CA 2D 6D 4A A2 4E 30 DC 73 17 05 
32 F3 58 71 28 0A C7 3A 45 E3 6C 70 EF 40 6A 09 
A5 AB 97 1A AF BB BE 76 C1 1B 9A 04 51 D6 15 BA 
66 23 AC EC E8 81 A1 25 24 EA 06 8C D2 AA DA D1 
08 B0 B5 0E B4 82 FF D3 BF B9 FB C5 FC 83 E2 8A 
i = 76, j = 171