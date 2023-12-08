from ltp import LTP

ltp = LTP()

def SEG():
    result = ltp.pipeline(["看了鲁元，也是贵相。"], tasks=["cws", "pos"])
    print(result.cws)
    print(result.pos)

def DP():
    result = ltp.pipeline(["看了鲁元，也是贵相。"], tasks=["cws", "dep"])
    print(result.dep)

def SRL():
    result = ltp.pipeline(['看了鲁元，也是贵相。'], tasks=["cws", "srl"])
    print(result.srl)

if __name__ == '__main__':
    SEG()
    DP()
    # SRL()