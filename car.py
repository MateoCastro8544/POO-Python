from lib2to3.pgen2 import driver

from account import Account


class Car :
    id          = str
    #tipo de dato cambiado en base a Account (primero se debe importar la informacion)
    driver      = Account ("","")
    passager    = int 
    license     = str
    
    def __init__(self, license, driver):
        self.license  = license
        self.driver   = driver
    