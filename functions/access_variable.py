jilaparsad = "ABC Person"

def village1():
    global jilaparsad
    sarpanch = "Sarpanch of Village1"
    print(sarpanch)
    print(jilaparsad+" Zilaparsad")    
    jilaparsad="XYZ Person"

def village2():
    sarpanch = "Sarpanch of Village2"
    print(sarpanch)
    print(jilaparsad+"Zilaparsad")

village1()
village2()
# print(sarpanch)