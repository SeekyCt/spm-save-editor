"""
Save Structure:
0000 - 25af   data
25b0 - 25b3   checksum
25b4 - 25b7   ~checksum
"""

SPMARIO_GLOBALS_OFFSET = 0x8
SPMARIO_GLOBALS_SIZE = 0x1b08

POUCH_WORK_OFFSET = 0x1b10
POUCH_WORK_SIZE = 0x6a0

POUCH_LEVEL_OFFSET  = POUCH_WORK_OFFSET + 0x4
POUCH_ATTACK_OFFSET = POUCH_WORK_OFFSET + 0x8
POUCH_HP_OFFSET     = POUCH_WORK_OFFSET + 0xc
POUCH_MAX_HP_OFFSET = POUCH_WORK_OFFSET + 0x10
POUCH_XP_OFFSET     = POUCH_WORK_OFFSET + 0x18
POUCH_COINS_OFFSET  = POUCH_WORK_OFFSET + 0x1c

SAVE_DATA_SIZE = 0x25b0
SAVE_FILE_SIZE = SAVE_DATA_SIZE + 8

def word(n):
    return int.to_bytes(n, 4, 'big')

class SaveWrapper:
    def __init__(self, filename=None):
        if filename is None:
            self.data = bytearray([0 for i in range(0, SAVE_DATA_SIZE)])
        else:
            f = open(filename, 'rb')
            dat = f.read()
            f.close()
            assert len(dat) == SAVE_FILE_SIZE, "Invalid sized save file"
            self.data = dat[0:SAVE_DATA_SIZE]

    def calcChecksum(self):
        s = 0
        for i in range(0, len(self.data)):
            s += self.data[i]
        s += 0 * 4 + 0xff * 4 # checksum & checksumNOT set to these for calculation
        return s & 0xffffffff

    def toBinary(self):
        checksum = self.calcChecksum()
        return bytearray(self.data + word(checksum) + word(~checksum & 0xffffffff))

    def writeWord(self, offset, val):
        b = word(val)
        self.data[offset] = b[0]
        self.data[offset+1] = b[1]
        self.data[offset+2] = b[2]
        self.data[offset+3] = b[3]
    
    def readWord(self, offset):
        b = self.data[offset:offset+4]
        return int.from_bytes(b, "big")
