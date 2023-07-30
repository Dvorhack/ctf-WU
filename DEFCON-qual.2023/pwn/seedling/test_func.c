#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>

typedef char *(*get_salt_t)(char*, FILE *, uint);

int main (int argc, char** argv) {

  void* handler = dlopen("./verify.patched", RTLD_LAZY);
  if (!handler) {
    fprintf(stderr, "dlopen error: %s\n", dlerror());
    return 1;
  }
  get_salt_t check_found = (get_salt_t)dlsym(handler, "get_salt");
  if(check_found == NULL){
    puts("Error finding the function");
    char *errstr;

    errstr = dlerror();
    if (errstr != NULL)
    printf ("A dynamic linking error occurred: (%s)\n", errstr);
    exit(0);
  }

  FILE *hashes_fd = fopen("hashes.txt","r");
  char * out= check_found("elf", hashes_fd, 0);

  printf("Output %s", out);

  return 0;
}