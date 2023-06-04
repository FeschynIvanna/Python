class InvalidPriceException(Exception):
    """Exception thrown if any of the pencil, pen, or eraser prices has an invalid value
     (for example, a negative value)."""

    def __init__(self, message="The price is wrong!"):
        self.message = message
        super().__init__(self.message)
