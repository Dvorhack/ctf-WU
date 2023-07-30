run:
	../run.sh ../initramfs.cpio exploit

debug:
	xfce4-terminal -e "gdb ../vmlinux -x ../gdb.sh"
	$(MAKE) run
