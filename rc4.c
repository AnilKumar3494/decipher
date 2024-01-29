#include <stdio.h>

void swap(unsigned char *a, unsigned char *b) {
    unsigned char temp = *a;
    *a = *b;
    *b = temp;
}

void rc4_initialize(unsigned char S[256], const unsigned char key[], int key_length) {
    int i, j;

    for (i = 0; i < 256; i++) {
        S[i] = i;
    }

    j = 0;
    for (i = 0; i < 256; i++) {
        j = (j + S[i] + key[i % key_length]) % 256;
        swap(&S[i], &S[j]);
    }
}

unsigned char rc4_generate_keystream(unsigned char S[256], int *i, int *j) {
    *i = (*i + 1) % 256;
    *j = (*j + S[*i]) % 256;

    swap(&S[*i], &S[*j]);

    return S[(S[*i] + S[*j]) % 256];
}

int main() {
    unsigned char key[] = {0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F, 0x77};
    int key_length = sizeof(key) / sizeof(key[0]);

    unsigned char S[256];
    int i = 0, j = 0;

    // a. Initialization phase
    rc4_initialize(S, key, key_length);

    printf("a. Permutation S after initialization:\n");
    for (int row = 0; row < 16; row++) {
        for (int col = 0; col < 16; col++) {
            printf("%02X ", S[row * 16 + col]);
        }
        printf("\n");
    }
    printf("i = %d, j = %d\n\n", i, j);

    // b. After generating the first 100 bytes of keystream
    printf("b. Permutation S after generating the first 100 bytes of keystream:\n");
    for (int k = 0; k < 100; k++) {
        rc4_generate_keystream(S, &i, &j);
    }
    for (int row = 0; row < 16; row++) {
        for (int col = 0; col < 16; col++) {
            printf("%02X ", S[row * 16 + col]);
        }
        printf("\n");
    }
    printf("i = %d, j = %d\n\n", i, j);

    // c. After generating the first 1000 bytes of keystream
    printf("c. Permutation S after generating the first 1000 bytes of keystream:\n");
    for (int k = 0; k < 900; k++) {
        rc4_generate_keystream(S, &i, &j);
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

