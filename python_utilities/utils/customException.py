class DirectoryNotFound(Exception):
    def __init__(self, _msg):
        self.msg = _msg
    pass

class ZeroByteSizeException(Exception):
    def __init__(self, _msg):
        self.msg = _msg
    pass

class FileNotFound(Exception):
    def __init__(self, _msg):
        self.msg = _msg
    pass

class CreateFolderException(Exception):
    def __init__(self, _msg):
        self.msg = _msg
    pass

class DeleteFolderException(Exception):
    def __init__(self, _msg):
        self.msg = _msg
    pass
