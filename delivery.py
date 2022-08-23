import order, deliverystatus, track, internal, position

class Delivery():
    def __init__(self) -> None:
        self.order = order.Order
        self.satus = deliverystatus.Deliverystatus
        self.track = track.Track
        self.driver = internal.Internal
        self.position = position.Position

    def watchposition():
        pass
    
    def getcurrentposition():
        pass

    def __setcurrentposition() -> None:
        pass