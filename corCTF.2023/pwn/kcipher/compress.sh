#!/usr/bin/env bash

if [ ! -d 'initramfs' ]; then
    echo 'Directory initramfs does not exists'
    exit -1
fi

cd initramfs
find . -print0 \
| cpio --null -ov --format=newc \
| gzip -9 > initramfs.cpio.gz
mv ./initramfs.cpio.gz ../