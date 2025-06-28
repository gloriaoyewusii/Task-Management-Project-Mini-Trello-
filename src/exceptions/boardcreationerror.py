class BoardCreationError(Exception):
    def __init__(self, message="An error occurred while creating a board"):
        super().__init__(message)