from brukstilfelle1.brukstilfelle1 import __init__ as b1
from brukstilfelle2.brukstilfelle2 import __init__ as b2
from brukstilfelle3.brukstilfelle3 import __init__ as b3
from brukstilfelle4.brukstilfelle4 import __init__ as b4
from brukstilfelle5.brukstilfelle5 import __init__ as b5
from brukstilfelle6.brukstilfelle6 import __init__ as b6
from brukstilfelle7.brukstilfelle7 import __init__ as b7

def main():
    b1()
    b2()
    b3()
    b4(input("Sett inn dato for brukstilfelle 4 (Format: ÅÅÅÅ-MM-DD): "))
    b5()
    b6()
    b7(input("Sett inn navn på skuespiller for brukstilfelle 7: "))

main()