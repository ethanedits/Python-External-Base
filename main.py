import pymem
from pymem.process import module_from_name

pm = pymem.Pymem("ac_client.exe")

gameModule = module_from_name(pm.process_handle, "ac_client.exe").lpBaseOfDll

def GetPtrAddr(base, offsets):
    addr = pm.read_int(base)
    for i in offsets:
        if i != offsets[-1]:
            addr = pm.read_int(addr + i)
    return addr + offsets[-1]

while True:
    pm.write_int(GetPtrAddr(gameModule + 0x0010F418, [0x40C, 0x168, 0x9C, 0xDC, 0x488]), 1337)
