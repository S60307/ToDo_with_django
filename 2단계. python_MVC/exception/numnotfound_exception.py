class NUMNotFoundException(Exception):
    def __init__(self, message) :
        print(message,type(message))
        super().__init__(message+" : 존재하지 않는 NUM")