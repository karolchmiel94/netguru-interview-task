class ModelNotFoundError(Exception):
    """No model has been found."""

    def __init__(self, message='Car with given Model does not exist for this Maker.'):
        self.message = message
        super().__init__()


class NoResultsError(Exception):
    """Car maker has not been found."""

    def __init__(self, message='No data. Check if Make name is valid.'):
        self.message = message
        super().__init__()


class VehicleAPIError(Exception):
    """Vehicle API returned error"""

    def __init__(self, message='Vehicle API returned error. Check if data is valid.'):
        self.message = message
        super().__init__()
