from car import Car

class UberConfort(Car):
    numberPassangers    = int
    carAcepted          = []
    seatMaterial        = []
    
    def __init__(self, license, driver, carAcepted, seatMaterial, numberPassangers):
        super().__init__(license, driver)
        self.carAcepted         = carAcepted
        self.seatMaterial       = seatMaterial
        self.numberPassangers   = numberPassangers