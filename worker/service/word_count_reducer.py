import os

class WordCountReducer:

    def __init__(self, worker_no, file_path, num_workers=3):
        self.file_path = file_path
        self.feature = "WordCount"
        self.worker_no = worker_no
        #self.key_mapping = key_mapping
        self.num_workers = num_workers

    def run(self):
        local_key_mapping = {}
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    words = line.split(',')
                    key = words[0]
                    value = int(words[1])

                    worker = abs(hash(key)) % self.num_workers + 1
                    print(f"Key: {key}, Value: {value}, Worker: {worker}, Current Worker: {self.worker_no}")
                    if worker == self.worker_no:
                        if key in local_key_mapping:
                            local_key_mapping[key] += 1
                        else:
                            local_key_mapping[key] = 1
        except Exception as e:
            print(e)

        return local_key_mapping

