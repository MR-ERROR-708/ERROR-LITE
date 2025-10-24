import platform
import os
import socket
import subprocess
import time
arc = None
os.system('clear')
print(f'\x1b[1;97m[\x1b[1;91m•\x1b[1;97m] \x1b[1;97mCHECKING FOR UPDATED')
os.system('git pull --qui_pet')

def main():
    global arc
    architecture = platform.architecture()
    if architecture[0] == '32bit':
        arc = "32BIT"
        print(f"\x1b[1;97m[\x1b[1;91m•\x1b[1;97m] \x1b[1;97m32BIT DETECTED")
        print(f"\x1b[1;97m[\x1b[1;91m•\x1b[1;97m] \x1b[1;97mSTARTING ERROR TOOL")
        time.sleep(5)
        os.system('chmod 777 ERROR32;./ERROR32')
    elif architecture[0] == '64bit':
        arc = "64BIT"
        print(f"\x1b[1;97m[\x1b[1;91m•\x1b[1;97m] \x1b[1;97m64BIT DETECTED")
        print(f"\x1b[1;97m[\x1b[1;91m•\x1b[1;97m] \x1b[1;97mSTARTING ERROR TOOL")
        time.sleep(5)
        os.system('chmod 777 ERROR64;./ERROR64')
    else:
        arc = "INVALID"
        print(f"\x1b[1;97m[\x1b[1;91m!\x1b[1;97m] \x1b[1;91mUNKNOWN DEVICE TYPE")
        exit()

if __name__ == "__main__":
    main()
