import invoice, creditcard

class Creditcard():
    invoices: invoice.Invoice
    __creditCard: creditcard.Creditcard

    def __init__(self, invoices, creditCard):
        self.invoices=invoices
        self.__creditCard=creditCard