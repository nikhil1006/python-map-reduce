import os

class WordCountReducer:

    def __init__(self, worker_no, file_path, key_mapping):
        self.file_path = file_path
        self.feature = "WordCount"
        self.worker_no = worker_no
        self.key_mapping = key_mapping

    def run(self):
        try:
            worker_no = int(os.getenv('workerNo'))
            with open(self.file_path, 'r') as file:
                for line in file:
                    words = line.split(',')
                    key = words[0]
                    value = int(words[1])

                    worker = abs(hash(key)) % 3 + 1
                    if worker == worker_no:
                        if key in self.key_mapping:
                            self.key_mapping[key] += 1
                        else:
                            self.key_mapping[key] = 1

        except Exception as e:
            print(e)

        return "Process Completed"
