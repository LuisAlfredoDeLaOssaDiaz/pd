import package

class Overweightpackage(package.Package):
    overweight: float
    def __init__(self, id, code, description, grams_price, base_price, weightKg, overweight):
        super().__init__(id, code, description, grams_price, base_price, weightKg)

        self.overweight=overweight

    def calculate(self) -> float:
        pass