import invoice, creditcard, location

class Customer(invoice.Invoice):
    def __init__(self, invoices, credit_card, shipping):
        self.invoices=invoice.Invoice
        self.credit_card=creditcard.Creditcard
        self.shipping=location.Location