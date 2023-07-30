# Write-ups CTF

Write-ups repo
## pwn
### stack
- simple BOF -> [HackSecuReims.2023/pwn/chat_not_gpt](./HackSecuReims.2023/pwn/chat_not_gpt/)
- ret2libm -> [IrisCTF.2023/pwn/ret2libm](./IrisCTF.2023/pwn/ret2libm/)
- ret2plt, ret2libc -> [la_ctf.2023/pwn/bot](./la_ctf.2023/pwn/bot/)
- stack pivot, ret2plt, ret2libc -> [la_ctf.2023/pwn/stuff](./la_ctf.2023/pwn/stuff/)
- basic PRNG break, ret2win -> [AmateursCTF.2023/pwn/rntk](./AmateursCTF.2023/pwn/rntk/)
- seccomp no write, blind brute force flag shellcode -> [midnightCTF.2023/pwn/c_est_con](./midnightCTF.2023/pwn/c_est_con/)
- basic ret2libc -> [midnightCTF.2023/pwn/babypwn](./midnightCTF.2023/pwn/babypwn/)
- fmt for canary then ret2plt ret2win -> [404CTF.2023/pwn/cohue](./404CTF.2023/pwn/cohue/)
- ret2dlresolve -> [404CTF.2023/pwn/feuille](./404CTF.2023/pwn/feuille/)
- brute force canary and libc, ret2libc -> [CrewCTF.2023/pwn/warmup](./CrewCTF.2023/pwn/warmup/)
- ret2plt, ret2libc with some contraints -> [angstromCTF.2023/pwn/widget](./angstromCTF.2023/pwn/widget/)
### misc
- one byte overflow -> [HackSecuReims.2023/pwn/configuration_loader](./HackSecuReims.2023/pwn/configuration_loader/)
- rust - c interconnexion -> [AmateursCTF.2023/pwn/ffi](./AmateursCTF.2023/pwn/ffi/)
- int type juggeling -> [AmateursCTF.2023/pwn/hex](./AmateursCTF.2023/pwn/hex/)
- exec elf with size constraint -> [AmateursCTF.2023/pwn/elf1](./AmateursCTF.2023/pwn/elf1/)
- int type juggeling -> [AmateursCTF.2023/pwn/hex2](./AmateursCTF.2023/pwn/hex2/)
### format string
- find libc, got overwrite -> [HackSecuReims.2023/pwn/rot13_as_a_service](./HackSecuReims.2023/pwn/rot13_as_a_service/)
- GOT overwrite -> [la_ctf.2023/pwn/rickroll](./la_ctf.2023/pwn/rickroll/)
- RELRO so ROP -> [la_ctf.2023/pwn/rut_roh_relro](./la_ctf.2023/pwn/rut_roh_relro/)
- GOT overwrite -> [midnightCTF.2023/pwn/tlv](./midnightCTF.2023/pwn/tlv/)
- leak stack, write shellcode dirents -> [404CTF.2023/pwn/citation](./404CTF.2023/pwn/citation/)
- ROP ret2libc -> [404CTF.2023/pwn/citation2](./404CTF.2023/pwn/citation2/)
- overwrite __free_hook -> [404CTF.2023/pwn/protocole](./404CTF.2023/pwn/protocole/)
- FULL RELRO, few space available -> [angstromCTF.2023/pwn/slack](./angstromCTF.2023/pwn/slack/)
### file struct
- leak with fwrite -> [IrisCTF.2023/pwn/babyseek](./IrisCTF.2023/pwn/babyseek/)
### shellcode
- basic open read write -> [AmateursCTF.2023/pwn/perm](./AmateursCTF.2023/pwn/perm/)
- egg hunting -> [AmateursCTF.2023/pwn/perfect_sandbox](./AmateursCTF.2023/pwn/perfect_sandbox/)
### heap
- fastbin dup -> [ImaginaryCTF.2023/pwn/mailman](./ImaginaryCTF.2023/pwn/mailman/)
- user after free -> [404CTF.2023/pwn/alchimiste](./404CTF.2023/pwn/alchimiste/)
- fastbin dup, tcache poisoning, leak environ, ROP, seccomp -> [CrewCTF.2023/pwn/company](./CrewCTF.2023/pwn/company/)
### kernel
- bypass kaslr, ROP -> [ImaginaryCTF.2023/pwn/opportunity](./ImaginaryCTF.2023/pwn/opportunity/)
- bypass kaslr, physmap -> [ImaginaryCTF.2023/pwn/opportunity](./ImaginaryCTF.2023/pwn/opportunity/)
### wasm
- simple overflow -> [404CTF.2023/pwn/tour_de_magie](./404CTF.2023/pwn/tour_de_magie/)
### VM
- custom VM -> [404CTF.2023/pwn/velocipede](./404CTF.2023/pwn/velocipede/)
## reverse
### packer
- multiple layer packer -> [404CTF.2023/rev/introspection](./404CTF.2023/rev/introspection/)
### keygen
- z3 contraints -> [404CTF.2023/rev/maj](./404CTF.2023/rev/maj/)
