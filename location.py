class Location():
    country: str
    state: str
    city: str
    addressline1: str
    addressline2: str
    zipcode: int

    def __init__(self, country, state, city, addressline1, addressline2, zipcode):
        self.country = country
        self.state = state
        self.city = city
        self.addressline1 = addressline1
        self.addressline2 = addressline2
        self.zipcode = zipcode