#include <stdio.h>
#include <stdlib.h>

// Disable ASLR for demo
// echo 0 | sudo tee /proc/sys/kernel/randomize_va_space # To disable
// echo 2 | sudo tee /proc/sys/kernel/randomize_va_space # To reenable

int main(void) {
    
    char buffer[200];

    printf("Send me your input!\n");

    fgets(buffer, 1024, stdin);
    return 0;
}
