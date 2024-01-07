# Write-ups CTF

Write-ups repo
## pwn
### format string
- leak et ret2main -> [LIT.2023/pwn/sprintf](./LIT.2023/pwn/sprintf/)
- overwrite __free_hook -> [404CTF.2023/pwn/protocole](./404CTF.2023/pwn/protocole/)
- ROP ret2libc -> [404CTF.2023/pwn/citation2](./404CTF.2023/pwn/citation2/)
- leak stack, write shellcode dirents -> [404CTF.2023/pwn/citation](./404CTF.2023/pwn/citation/)
- FULL RELRO, few space available -> [angstromCTF.2023/pwn/slack](./angstromCTF.2023/pwn/slack/)
- RELRO so ROP -> [la_ctf.2023/pwn/rut_roh_relro](./la_ctf.2023/pwn/rut_roh_relro/)
- GOT overwrite -> [la_ctf.2023/pwn/rickroll](./la_ctf.2023/pwn/rickroll/)
- GOT overwrite -> [midnightCTF.2023/pwn/tlv](./midnightCTF.2023/pwn/tlv/)
- find libc, got overwrite -> [HackSecuReims.2023/pwn/rot13_as_a_service](./HackSecuReims.2023/pwn/rot13_as_a_service/)
### misc
- int overflow, function poiner exploit, format string -> [LIT.2023/pwn/sha_sha_shell](./LIT.2023/pwn/sha_sha_shell/)
- patch binary -> [FCSC.2020/pwn/Patchinko](./FCSC.2020/pwn/Patchinko/)
- exec elf with size constraint -> [AmateursCTF.2023/pwn/elf1](./AmateursCTF.2023/pwn/elf1/)
- int type juggeling -> [AmateursCTF.2023/pwn/hex2](./AmateursCTF.2023/pwn/hex2/)
- int type juggeling -> [AmateursCTF.2023/pwn/hex](./AmateursCTF.2023/pwn/hex/)
- rust - c interconnexion -> [AmateursCTF.2023/pwn/ffi](./AmateursCTF.2023/pwn/ffi/)
- one byte overflow -> [HackSecuReims.2023/pwn/configuration_loader](./HackSecuReims.2023/pwn/configuration_loader/)
### kernel
- ROP in syscall, remove module -> [FCSC.2020/pwn/Hello-Rootkitty](./FCSC.2020/pwn/Hello-Rootkitty/)
- just do a syscall -> [FCSC.2020/pwn/Pepin](./FCSC.2020/pwn/Pepin/)
- shellcode edit syscall table -> [FCSC.2020/pwn/Hello-Rootkitty-harder](./FCSC.2020/pwn/Hello-Rootkitty-harder/)
- kernel heap UAF, dump ramfs -> [corCTF.2023/pwn/kcipher](./corCTF.2023/pwn/kcipher/)
- qemu monitor available -> [corCTF.2023/pwn/zeroday](./corCTF.2023/pwn/zeroday/)
- bypass kaslr, ROP -> [ImaginaryCTF.2023/pwn/opportunity](./ImaginaryCTF.2023/pwn/opportunity/)
- bypass kaslr, physmap -> [ImaginaryCTF.2023/pwn/opportunity](./ImaginaryCTF.2023/pwn/opportunity/)
### heap
- UAF -> [FCSC.2023/pwn/robot](./FCSC.2023/pwn/robot/)
- fastbin dup -> [ImaginaryCTF.2023/pwn/mailman](./ImaginaryCTF.2023/pwn/mailman/)
- user after free -> [404CTF.2023/pwn/alchimiste](./404CTF.2023/pwn/alchimiste/)
- fastbin dup, tcache poisoning, leak environ, ROP, seccomp -> [CrewCTF.2023/pwn/company](./CrewCTF.2023/pwn/company/)
### stack
- ret2dlresolve -> [ImaginaryCTF.2023/pwn/minimal](./ImaginaryCTF.2023/pwn/minimal/)
- fmt for canary then ret2plt ret2win -> [404CTF.2023/pwn/cohue](./404CTF.2023/pwn/cohue/)
- ret2dlresolve -> [404CTF.2023/pwn/feuille](./404CTF.2023/pwn/feuille/)
- basic PRNG break, ret2win -> [AmateursCTF.2023/pwn/rntk](./AmateursCTF.2023/pwn/rntk/)
- ret2plt, ret2libc with some contraints -> [angstromCTF.2023/pwn/widget](./angstromCTF.2023/pwn/widget/)
- ret2plt, ret2libc -> [la_ctf.2023/pwn/bot](./la_ctf.2023/pwn/bot/)
- stack pivot, ret2plt, ret2libc -> [la_ctf.2023/pwn/stuff](./la_ctf.2023/pwn/stuff/)
- brute force canary and libc, ret2libc -> [CrewCTF.2023/pwn/warmup](./CrewCTF.2023/pwn/warmup/)
- ret2libm -> [IrisCTF.2023/pwn/ret2libm](./IrisCTF.2023/pwn/ret2libm/)
- seccomp no write, blind brute force flag shellcode -> [midnightCTF.2023/pwn/c_est_con](./midnightCTF.2023/pwn/c_est_con/)
- basic ret2libc -> [midnightCTF.2023/pwn/babypwn](./midnightCTF.2023/pwn/babypwn/)
- simple BOF -> [HackSecuReims.2023/pwn/chat_not_gpt](./HackSecuReims.2023/pwn/chat_not_gpt/)
### wasm
- simple overflow -> [404CTF.2023/pwn/tour_de_magie](./404CTF.2023/pwn/tour_de_magie/)
### VM
- custom VM -> [404CTF.2023/pwn/velocipede](./404CTF.2023/pwn/velocipede/)
### shellcode
- egg hunting -> [AmateursCTF.2023/pwn/perfect_sandbox](./AmateursCTF.2023/pwn/perfect_sandbox/)
- basic open read write -> [AmateursCTF.2023/pwn/perm](./AmateursCTF.2023/pwn/perm/)
### file struct
- leak with fwrite -> [IrisCTF.2023/pwn/babyseek](./IrisCTF.2023/pwn/babyseek/)
## reverse
### keygen
- z3 contraints -> [404CTF.2023/rev/maj](./404CTF.2023/rev/maj/)
- z3 conditions with LShR, If and ZeroExt -> [ECW_finales.2023/rev/Super_Secure](./ECW_finales.2023/rev/Super_Secure/)
### packer
- multiple layer packer -> [404CTF.2023/rev/introspection](./404CTF.2023/rev/introspection/)
