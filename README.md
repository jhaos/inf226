# inf226
## Assignment 1

```C
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

int main( int argc , char * * argv ) {

char buffer [ 3 2 ] ;
int32_t check = 0xdeadbeef ;

printf("Try to get past me!\n");
fflush(stdout);

assert(fgets(buffer, 1024, stdin)!= NULL);

if(check == 0xc0cac01a){
  printf("Congratulations, you win!\n");
  fflush(stdout);
  system("cat flag.txt");
}
else {
  printf("You lose! Bye.\n");
}

return 0 ;
}
```
