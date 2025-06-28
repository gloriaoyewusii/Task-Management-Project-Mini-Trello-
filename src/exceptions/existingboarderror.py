class ExistingBoardError(Exception):
    def __init__(self, message="Board exists already"):
        super().__init__(message)