class Reduce:
    def __init__(self, feature=None, intermediate_files=None, misc=None):
        self.feature = feature
        self.intermediate_files = intermediate_files if intermediate_files is not None else []
        self.misc = misc

    def __str__(self):
        return f"Reduce{{feature='{self.feature}', intermediate_files={self.intermediate_files}, misc='{self.misc}'}}"
