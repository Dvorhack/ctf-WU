[bits 64]
file_load_va: equ 4096 * 40

db 0x7f, 'E', 'L', 'F'
entry_point:
  inc al
  mov esi, file_load_va + message
pass2:
  xor edi, 1
  jmp code_chunk_2
dw 2
dw 0x3e
code_chunk_2:
  mov dl, message_length
  jmp code_chunk_3
dq entry_point + file_load_va
dq program_headers_start
code_chunk_3:
  syscall
  mov al, 60
  jmp pass2
db 0 ; usable
db 0 ; usable
db 0 ; usable
program_headers_start:
dd 1 ; Program header type: must be 1 (loadable segment)
db 0x5 ; Program header flags: low bits must be 5 (readable and executable); high bytes don't matter
dw 0x38
dw 1
; High 7 bytes of offset of loadable segment
db 0
db 0
db 0
db 0
db 0
db 0
db 0
dq file_load_va ; Address in memory to load the segment into ; could change
message_length: equ 14
message:
db `Hello, w`
; size in file then size in memory; can be anything non-zero and equal
last_bytes: equ `orld!\n`
dq last_bytes
dq last_bytes
dq 0 ; alignment; usable
