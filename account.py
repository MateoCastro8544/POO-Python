

class Account :
    id          = int 
    name        = str
    document    = int 
    mail        = str
    password    = str 
    
    #metodo constructor Python 
    def __init__(self, name, document):
        self.name       = name
        self.document   = document