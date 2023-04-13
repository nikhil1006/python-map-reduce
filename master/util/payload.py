class Payload:
    def __init__(self, file_name=None, misc=None):
        self.file_name = file_name
        self.misc = misc

    def __repr__(self):
        return f"Payload(file_name='{self.file_name}', misc='{self.misc}')"
