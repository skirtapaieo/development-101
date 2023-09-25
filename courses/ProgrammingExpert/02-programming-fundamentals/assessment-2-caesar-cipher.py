

def caesar_cipher(string, offset):
    output = ''
    for char in string:
        ascii_val = ord(char)
        ascii_val -= offset
        if ascii_val < ord('a'):
            ascii_val += 26
        output += chr(ascii_val)
    return output
