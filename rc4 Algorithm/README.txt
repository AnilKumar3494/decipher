RC4 - Rivest Cipher 4 is a form of stream cipher that encrypts messages one byte at a time

## Executing the code
If on a local system make sure we have gcc - for c programming
(or)
Alternatively, we can use any online compiler to run the code


## Implementing the Algorithm

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