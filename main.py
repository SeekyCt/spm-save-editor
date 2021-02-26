from os import system
from SaveWrapper import *

save = SaveWrapper(input("Save file path: "))
f = open(input("Output file path: "), 'wb')

print("---Current Stats---")
print(f"Level is {save.readWord(POUCH_LEVEL_OFFSET)}")
print(f"XP is {save.readWord(POUCH_XP_OFFSET)}")
print(f"HP is {save.readWord(POUCH_HP_OFFSET)}")
print(f"Max HP is {save.readWord(POUCH_MAX_HP_OFFSET)}")
print(f"Attack is {save.readWord(POUCH_ATTACK_OFFSET)}")
print(f"Coins is {save.readWord(POUCH_COINS_OFFSET)}")

print("---New Stats---")
save.writeWord(POUCH_LEVEL_OFFSET,  int(input("Level: ")))
save.writeWord(POUCH_XP_OFFSET,     int(input("XP: ")))
save.writeWord(POUCH_HP_OFFSET,     int(input("HP: ")))
save.writeWord(POUCH_MAX_HP_OFFSET, int(input("Max HP: ")))
save.writeWord(POUCH_ATTACK_OFFSET, int(input("Attack: ")))
save.writeWord(POUCH_COINS_OFFSET,  int(input("Coins: ")))

f.write(save.toBinary())
f.close()
print("File saved!")
