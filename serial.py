import wiringpi
import struct
import logging


class Serial(object):

    def __init__(self, tty, baudrate, timeout):

        self.serial = wiringpi.Serial(tty, baudrate)

    def open(self):
        pass

    def write(self, packed_data):
        chars = struct.unpack('B' * len(packed_data), packed_data)
        for c in chars:
            self.serial.putchar(c)

    def read(self, num_bytes):
        read_val = ""
        for i in range(num_bytes):
            new_char = chr(self.serial.getchar())
            read_val += new_char
        return read_val

    def setRTS(self, val):
        pass
