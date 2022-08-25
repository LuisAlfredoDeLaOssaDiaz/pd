from enum import Enum

class Invoicestatus(Enum):
    PROCESSING: str
    SENT: str
    REJECTED: str
    CANCELLED: str
