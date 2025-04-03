import time
from pathSetup import *
from sysInit import sysInit1, sysInit2

def appInit() :
    
    print("Proc Id:::::", sysInit1.initId1)
    sysInit1.init1()
    time.sleep(1.5)
    print("Proc Id:::::", sysInit2.initId2)
    sysInit2.init2()
    time.sleep(1.5)
    
    print("appInit Complete!!!")
    time.sleep(2)    
    print(":::::::::::::::::::")