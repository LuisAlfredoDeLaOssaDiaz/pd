# # from abc import ABC, abstractmethod
from customer import Customer

class Package():
    id:str
    code:int
    description:str
    grams_price:float
    base_price:float
    weightKg:float
    customer:Customer

    def __init__(self, id, code, description, grams_price, base_price, weightKg):
        self.id=id
        self.code=code
        self.description=description
        self.grams_price=grams_price
        self.base_price=base_price
        self.weightKg=weightKg
        self.customer=Customer

    def calculate(self):
        calculate = self.weightKg*1000
        # print(f'El pesoi en gramos: {calculate} ')
        pass



# kevin=Package("1",1,"1",1,1,10)
# kevin.Calculate()


