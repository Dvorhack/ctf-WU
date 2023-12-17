#!/usr/bin/env bash

mkdir -p initramfs
cd initramfs
gunzip -c ../initramfs.cpio.gz | cpio -idv
