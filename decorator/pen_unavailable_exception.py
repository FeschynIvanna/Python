class PenUnavailableException(Exception):
    """An exception that occurs if the pen in the pencil case is not available or has expired."""

    def __init__(self, message="Out of pens!"):
        self.message = message
        super().__init__(self.message)
