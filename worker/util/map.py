class Map:
    def __init__(self, feature=None, file_name=None, start_no=None, end_no=None, misc=None):
        self.feature = feature
        self.file_name = file_name
        self.start_no = start_no
        self.end_no = end_no
        self.misc = misc

    def __str__(self):
        return f"Map{{feature='{self.feature}', file_name='{self.file_name}', start_no={self.start_no}, end_no={self.end_no}, misc='{self.misc}'}}"
