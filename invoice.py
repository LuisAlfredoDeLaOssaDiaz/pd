import order, invoicestatus, customer, paymentmethodtypes

class Invoice():
    id: str
    orders: order.Order
    status: invoicestatus.Invoicestatus
    client: customer.Customer
    tax: float
    price: float
    pirce: float
    discoint: float
    paymentmethod: paymentmethodtypes.Paymentmethodtypes

    def __init__(self) -> None:
        self.id = id
        self.orders = order.Order
        self.status = invoicestatus.Invoicestatus
        self.client = customer.Customer
        self.tax = float
        self.price = float
        self.pirce = float
        self.discoint = float
        self.paymentmethod = paymentmethodtypes.Paymentmethodtypes