enc = open("enc").read
for c in enc:
    print(hex(ord(c)).lstrip("0x"), end='')

This code converts each character c in enc to:
Its Unicode code point using ord(c)
Then to hexadecimal using hex(...)
Then it strips the "0x" prefix using .lstrip("0x")
Finally, it prints all the hex characters in a single line with end=''

picoCTF{16_bits_inst34d_of_8_04c0760d}
