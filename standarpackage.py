from package import Package

class Standardpackage(Package):
    quota: float
    def __init__(self, id, code, description, grams_price, base_price, weightKg, quota):
        super().__init__(id, code, description, grams_price, base_price, weightKg)

        self.quota=quota
    
    def calculate(self):
        return super().calculate()
