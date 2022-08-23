import overweightpackage, package


id = str(input("Ingrese el id: "))
cod = int(input("Ingrese el code: "))
description = str(input("Ingrese el description: "))
grams_price = float(input("Ingrese el grams_price: "))
base_price = float(input("Ingrese el base_price: "))
weightKg = float(input("Ingrese el weightKg: "))


kevin=overweightpackage.Overweightpackage(id, cod, description, grams_price, base_price, weightKg, 500)
kevin.Calculate()

