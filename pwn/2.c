#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

void do_system() {
    system("cat flag.txt");
}

int main(int argc, char **argv) {
    
    char buffer[32];

    printf("Try to get past me!\n");
    fflush(stdout);

    assert(fgets(buffer, 1024, stdin) != NULL);

    return 0;
}
