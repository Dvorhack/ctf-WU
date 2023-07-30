from pwn import *
elf = context.binary = ELF('./introspection')

# List symbols at program
for key, address in elf.symbols.items():
    print(key, hex(address))

#Nulify alarm function
elf.asm(elf.symbols['ptrace'], 'mov rax, 0\nret')
elf.save('./newbinary')