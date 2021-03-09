class NoPointsToConnectException(Exception):
    def __init__(self):
        super().__init__("No points provided in the given file")


class WrongEntryFileFormat(Exception):
    def __init__(self, msg):
        super().__init__(msg)
