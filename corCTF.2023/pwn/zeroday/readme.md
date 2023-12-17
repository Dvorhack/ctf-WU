# zeroday
by: *clubby789, FizzBuzz101*  
25 solves / 220 points

## Description
corCTF is proud to introduce our new zero-day submission service. Simply test out your 0-days here, and we will sell evaluate them for you.

NOTE: exploiting zero-days in the service is not allowed! our run configuration is proprietary, so please do not monitor or look at it!

## Exploit
The Qemu monitor isn't nulled (`-monitor /dev/null`) so we can enter in monitor using `Ctrl-a + c`

Because we are using a ramfs, the **flag.txt** is in ram.  
With `info mtree`, we can see that cpu ram is at physical addr 0 so we can dump it using `px/x @addr` and grep for the flag