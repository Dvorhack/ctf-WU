## Notes
To load the kernel into gdb we need the vmlinux  
```bash
wget https://raw.githubusercontent.com/torvalds/linux/master/scripts/extract-vmlinux
extract-vmlinux ./bzimage > vmlinux
```

To modify the initramfs we can decompress, modify and compress.  
Usefull modifications for debugging: 
- `/etc/initRC`:
    - run shell as root
    - enable `/etc/kallsyms`
- qemu:
    - disable kaslr: kernel option `nokaslr`