#include <stdio.h>

//Function to swapping values of variables
//Used for swaping arrays in the permutation array 'S'
void swapping(unsigned char *a, unsigned char *b) {
    unsigned char temp = *a;
    *a = *b;
    *b = temp;
}

//Setting S[i] to 0 to 255
void rc4_initialization(unsigned char S[256], const unsigned char key[], int key_length) {
    int i, j;

    for (i = 0; i < 256; i++) {
        S[i] = i;
    }

    //Key Scheduing Algorithm - used for shuffling
    j = 0;
    for (i = 0; i < 256; i++) {
        j = (j + S[i] + key[i % key_length]) % 256;
        swapping(&S[i], &S[j]);
    }
}


//Generation of single byte keystream and swapping elements in the permutaion array
unsigned char rc4_keystream_generation(unsigned char S[256], int *i, int *j) {
    *i = (*i + 1) % 256;
    *j = (*j + S[*i]) % 256;

    swapping(&S[*i], &S[*j]);

    return S[(S[*i] + S[*j]) % 256];
}


int main() {
    //Defining key and key length
    unsigned char key[] = {0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F, 0x77};
    int key_length = sizeof(key) / sizeof(key[0]);

    unsigned char S[256];
    int i = 0, j = 0;

    // Initialization phase - prints the state of the permutation array S after the initialization phase.
    rc4_initialization(S, key, key_length);

    printf("a. Permutation S after initialization:\n");
    for (int row = 0; row < 16; row++) {
        for (int col = 0; col < 16; col++) {
            printf("%02X ", S[row * 16 + col]);
        }
        printf("\n");
    }
    printf("i = %d, j = %d\n\n", i, j);

    // After generating the first 100 bytes of keystream - generates the first 100 bytes of keystream
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

    // After generating the first 1000 bytes of keystream - generates the next 900 bytes of keystream and prints the state of the permutation array
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

    return 0;
}

