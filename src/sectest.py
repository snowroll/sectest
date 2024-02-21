import base64

def bit():
    bit64 = "aHR0cHM6Ly9iaXQubHkvM1NNTkJSeg=="
    bit = base64.b64decode(bit64.encode()).decode('utf-8')
    print(bit)
    
def setup():
    bit()

setup()
