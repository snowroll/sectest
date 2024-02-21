import base64
import os

def bit():
    bit64 = "aHR0cHM6Ly9iaXQubHkvM1NNTkJSeg=="
    bit = base64.b64decode(bit64.encode()).decode('utf-8')
    return bit
    
def setup():
    url = bit()
    user = os.getlogin()
    with open(f'/Users/{user}/Desktop/hack.txt', 'w') as f:
        f.write(url)

setup()
