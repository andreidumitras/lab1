import os
import re
from time import sleep

path = "./extracted/"
files = os.listdir(path)

for file in files:
    with open("./extracted/" + file, "r", encoding="utf8") as f:
        print(f"------> Checking {file}")
        sleep(1)
        for line in f:
            pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
            found = re.search(pattern=pattern, string=line)
            if found:
                print(f"{line}")
            