import package, customer, orderstatus, location


class Order():
    id:str
    packag_:package.Package
    paid:float
    receiver:customer.Customer
    sender:customer.Customer
    status:orderstatus.Orderstatus
    location: location.Location

    def __init__(self, id, paid):
        self.id= id
        self.packag_ = package.Package
        self.paid= paid
        self.receiver= customer.Customer
        self.sender= customer.Customer
        self.status= orderstatus.Orderstatus
        self.location_= location.Location