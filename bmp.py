import sys


def write(bb: bytes):
    sys.stdout.buffer.write(bb)


def u8(i: int):
    write(i.to_bytes(4, 'little'))


def u16(i: int):
    write(i.to_bytes(2, 'little'))


def u32(i: int):
    write(i.to_bytes(4, 'little'))


def rgb(red: int, green: int, blue: int):
    u8(blue)
    u8(green)
    u8(red)


WIDTH = 128
HEIGHT = 128

# file header (14 bytes)
write(b"BM") # magic
u32(14 + 40 + WIDTH * HEIGHT * 3)
u32(0)
u32(14 + 40)

# dib header (40 bytes)
u32(40) # size of dib header
u32(WIDTH)
u32(HEIGHT)
u16(1)
u16(24)
u32(0)
u32(0)
u32(0)
u32(0)
u32(0)
u32(0)

for py in range(HEIGHT):
    for px in range(WIDTH):
        rgb(255, 0, 0)