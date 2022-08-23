# from abc import ABC, abstractmethod
# from .enumerate import PersonType
# from abc import ABC, abstractmethod
import location

class Person():
    id:str
    nationalidad:str
    id_type:str
    person_type:str
    name:float
    email:float
    last_name:str
    location: location.Location
    
    def __init__(self, id, nationalidad, id_type, person_type, name, email, last_name ):
        self.id = id
        self.nationalidad = nationalidad
        self.id_type = id_type
        self.person_type = person_type
        self.name = name
        self.email = email
        self.last_name = last_name
        location: location.Location