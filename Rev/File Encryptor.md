Wrote a program to decrypt the file after analyzing.

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void decryptor(long param_1, ulong param_2);

int main(int argc, char *argv[]) {
    // Define the input file name
    const char *file_name = "flag.bin";

    // Open the file in read-binary mode
    FILE *file = fopen(file_name, "rb");
    if (!file) {
        printf("No such file exists\n");
        return 1;
    }

    // Seek to the end of the file to determine its size
    fseek(file, 0, SEEK_END);
    size_t file_size = ftell(file);
    fseek(file, 0, SEEK_SET);

    // Allocate memory to hold the file contents
    void *buffer = malloc(file_size);
    if (!buffer) {
        printf("malloc() failed\n");
        fclose(file);
        return 1;
    }

    // Read the file contents into the buffer
    fread(buffer, 1, file_size, file);
    fclose(file);

    // Seed the random number generator with the same seed used for encryption
    srand(0x1337);
    // Decrypt the contents of the buffer
    decryptor((long)buffer, file_size);

    // Define the output file name
    const char *decrypted_file_name = "flag.decrypted";

    // Open the output file in write-binary mode
    file = fopen(decrypted_file_name, "wb");
    if (!file) {
        printf("Failed to create decrypted file\n");
        free(buffer);
        return 1;
    }

    // Write the decrypted contents to the output file
    fwrite(buffer, 1, file_size, file);
    fclose(file);

    // Free the allocated memory
    free(buffer);

    // Print success message
    printf("Decryption successful. \nDecrypted file: %s\n", decrypted_file_name);

    return 0;
}

// Decryptor function that reverses the encryption logic
void decryptor(long param_1, ulong param_2) {
    int iVar1;
    int local_10;
    int local_c;

    for (local_c = 0; (ulong)(long)local_c < param_2; local_c = local_c + 8) {
        for (local_10 = 0; (local_10 < 8 && ((ulong)(long)(local_10 + local_c) < param_2)); local_10 = local_10 + 1) {
            iVar1 = local_c;
            if (local_c < 0) {
                iVar1 = local_c + 7;
            }
            if ((iVar1 >> 3 & 1U) == 0) {
                iVar1 = rand();
                *(char *)(param_1 + (local_10 + local_c)) =
                    *(char *)(param_1 + (local_10 + local_c)) - (char)(iVar1 % 0xff);
            } else {
                iVar1 = rand();
                *(char *)(param_1 + (local_10 + local_c)) =
                    *(char *)(param_1 + (local_10 + local_c)) + (char)(iVar1 % 0xff);
            }
        }
    }
}                                                                                      
```

Ran the program and got the flag.

Flag:
```
ThunderCipher{W0W_Y0U_C4N_D3CRYPT_N0W_G0_SUBM1T_TH15!!!}
```