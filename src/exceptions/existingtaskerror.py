class ExistingTaskError(Exception):
    def __init__(self, message="Task exists already"):
        self.message = message