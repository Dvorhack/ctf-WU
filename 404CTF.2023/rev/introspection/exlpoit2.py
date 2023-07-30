import tqdm
from pwn import u32
import re, os
from subprocess import Popen, PIPE

START = b'\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00>\x00\x01\x00\x00\x00\xb0\x10\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00'

def decrypt(data,added):
    prog = b''
    for i in tqdm.tqdm(range(len(data))):
        prog += ( added[i % len(added)] ^ data[i]).to_bytes(1,'little')
    return prog

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def find_ADDED_off(content, data_o):
    data = content[data_o:data_o+len(START)]

    to_find = b''
    for i,e in enumerate(START):
        to_find += ((e ^  data[i]) % 256).to_bytes(1,'little')

    a = list(find_all(content, to_find))
    
    return a[-1]

def find_offsets(filename):
    content = open(filename,'r').read()


    off = re.findall('DAT_([a-f0-9]*)',content)

    print(off)

    if '0010200d' in off and len(off) == 11:
        off.remove('0010200d')

    assert len(off) == 10, f"Wrong offsets {off}"

    DECALAGE = 0X00101000
    data_len_o = int(off[3],16) - DECALAGE
    data_o = int(off[4],16) - DECALAGE
    added_len_o = int(off[6],16) - DECALAGE
    added_o = int(off[5],16) - DECALAGE

    print(hex(data_o), hex(data_len_o), hex(added_o), hex(added_len_o))

    return data_o, data_len_o, added_o, added_len_o

def get_values_from_offset(fname, data_o, data_len_o, added_o, added_len_o):
    content = open(fname,'rb').read()

    data_len = u32(content[data_len_o:data_len_o+4])
    data = content[data_o:data_o+data_len]

    added_len = u32(content[added_len_o:added_len_o+4])
    added = content[added_o:added_o+added_len]

    print(hex(data_len), data[:10])
    print(hex(added_len), added[:10])

    return data, data_len, added, added_len

def ghidra_analysis(i):
    if not os.path.isfile(f'outs/{i}_decompiled.c'):
        Popen(f'/opt/ghidra/support/analyzeHeadless ghidra ctf -import outs/{i}.elf -scriptPath ghidra-headless-scripts -postscript decompiler.py outs/{i}_decompiled.c'.split())
        input()
        print('Analysis done')
    # /opt/ghidra/support/analyzeHeadless /home/paul/Downloads/elligson/ghidra ctf -import ./toto -scriptPath ghidra-headless-scripts -postscript decompiler.py decompiled_malware_sample.c


out = b'\x7fELF\x02\x01\x01\x00\x00\x00'
i = 2
while out[:10] == b'\x7fELF\x02\x01\x01\x00\x00\x00':
    ghidra_analysis(i)

    data_o, data_len_o, added_o, added_len_o = find_offsets(f'outs/{i}_decompiled.c')
    data, data_len, added, added_len = get_values_from_offset(f'outs/{i}.elf', data_o, data_len_o, added_o, added_len_o)

    out = decrypt(data,added)

    print(out[:10])

    i += 1

    open(f'outs/{i}.elf','wb').write(out)