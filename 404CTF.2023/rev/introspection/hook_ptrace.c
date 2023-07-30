// gcc hook_ptrace.c -shared -o hook_ptrace

#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <linux/ptrace.h>

int status = -1;
 
int ptrace(int a, int b, void *c, void*d) {

    FILE *f;
    int count;
    f = fopen("/tmp/count","r");
    fscanf(f,"%d",&count);
    fclose(f);

    count++;
    printf("Count: %d\n",count);

    if (count == 202)
    {
        printf("Pid: %d\n", getpid());
        sleep(200);
    }
    

    f = fopen("/tmp/count","w");
    fprintf(f, "%d", count);
    fclose(f);


    if (a != PTRACE_TRACEME)
        return 0;

    if (status == -1)
        status = 0;
    else
        status = -1;
   
   return status;
}