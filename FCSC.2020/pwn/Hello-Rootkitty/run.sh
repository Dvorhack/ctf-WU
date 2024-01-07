#!/usr/bin/env bash

TEMP=/tmp/shm

echo "-----------------------------------------------------------------------------"
echo "To ease your exploit development, a secret folder shared between the host and"
echo "the vm will be created. You can access it at /mnt/share within the vm, and at"
echo "${TEMP} in the host. The folder will be deleted afterwards."
echo "-----------------------------------------------------------------------------"
echo ""

qemu-system-x86_64         \
    -m 64M                                                            \
    -cpu kvm64                                                        \
    -kernel bzImage                                         \
    -nographic                                                        \
    -append 'console=ttyS0 loglevel=3 oops=panic panic=1 kaslr nopti' \
    -initrd initramfs.cpio.gz                                  \
    -monitor /dev/null                                                \
    -fsdev local,id=exp1,path=${TEMP},security_model=mapped           \
    -device virtio-9p-pci,fsdev=exp1,mount_tag=ecsc \
    -no-reboot \
    -S -s
