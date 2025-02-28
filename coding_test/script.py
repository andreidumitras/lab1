import os
import zipfile
import zlib

path = "./archives/"
archives = os.listdir(path)

passwords = [
    "day26/dk",
    "Kuyo7110",
    "bamsunholyunion=)",
    "stnlycup#9",
    "ditmer2525",
    "ZANY123",
    "mcr0133050234",
    "crunkco010",
    "821574t",
    "allan8403",
]

for archive in archives:
    with zipfile.ZipFile('./archives/' + archive, 'r') as zip_arch:
        with open('rockyou_small.txt', 'r') as rockyou:
            for linepass in rockyou:
                try:
                    password = linepass.rstrip('\n')
                    zip_arch.extractall(path='./extracted/', pwd=password.encode('ascii'))
                    print(f"{archive} was unzipped with password: {password}")
                    break
                except RuntimeError:
                    pass
                except zlib.error:
                    pass
                except zipfile.BadZipFile:
                    pass
            

a = 4
b = a

a is b