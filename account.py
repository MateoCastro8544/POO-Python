

from typing_extensions import Self


class Account :
    id          = int 
    name        = str
    document    = int 
    mail        = str
    password    = str 
    
    def __init__(self, name, document):
        self.name       = name
        self.document   = document