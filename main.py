

from account import Account
from car import Car
from payment import Payment
from trip import Trip


if __name__ == "__main__":
    print("Hello world")
    
   ## carro = Car()
   ## carro.id            = 5
   ## carro.brand         = "Toyota"
   ## carro.driver        = "David"
   ## carro.passager      = 5
   ## 
   ## print (vars(carro))
   ## 
   ## carro2 = Car()
   ## carro2.id            = 3
   ## carro2.brand         = "chevrolet"
   ## carro2.driver        = "karina"
   ## carro2.passager      = 10
   ## 
   ## print (vars(carro2))
   ## 
   ## cuenta = Account()
   ## cuenta.id             = 5
   ## cuenta.name           = "David"
   ## cuenta.document       = "1728548544"
   ## cuenta.mail           = "david@gmail.com"
   ## cuenta.password       = "Admin"
   ## 
   ## print (vars(cuenta))
   ## 
   ## pago = Payment()
   ## pago.id         = 5
   ## pago.ammount    = 35
   ## 
   ## print (vars(pago))
   ## 
   ## viaje = Trip()
   ## viaje.id            =10
   ## viaje.user          = "david"
   ## viaje.car           ="uber x" 
   ## viaje.route         = "quito - guayaquil"
   ## viaje.amount        = 30,4
   ## viaje.payment       = "efectivo"
   ## viaje.progress      ="cerca del destino"
   ## viaje.completed     = "True"
   ## 
   ## print (vars(viaje))
         
    car = Car ("PBO5555", Account ("David Castro","1728548544"))
    
    print(vars(car))
    print(vars(car.driver))
    
    
    
    

    