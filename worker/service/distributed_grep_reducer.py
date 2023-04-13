import os
from concurrent.futures import ThreadPoolExecutor, as_completed

class DistributedGrepReducer:

    def __init__(self, file_path, feature, worker_no, key_mapping):
        self.file_path = file_path
        self.feature = feature
        self.worker_no = worker_no
        self.key_mapping = key_mapping

    def run(self):
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    words = line.strip().split(',')
                    key = words[0]
                    value = words[1]
                    worker = abs(hash(key)) % 3 + 1
                    if worker == self.worker_no:
                        self.key_mapping[key] = value

        except Exception as e:
            print(e)
        
        return "Process Completed"
