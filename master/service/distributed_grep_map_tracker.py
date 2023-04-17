import requests
from concurrent.futures import Future

class DistributedGrepMapTracker(Future):
    def __init__(self, worker_port, start_line, end_line, file_name, feature, input_parameter=None):
        super().__init__()
        self.worker_port = worker_port
        self.start_line = start_line
        self.end_line = end_line
        self.file_name = file_name
        self.feature = feature
        self.input_parameter = input_parameter

    def run(self):
        url = f'http://127.0.0.1:{self.worker_port}/mapProcess'

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        data = {
            'feature': 'DistributedGrep',
            'fileName': self.file_name,
            'startNo': self.start_line,
            'endNo': self.end_line,
            'misc': self.input_parameter,
        }

        response = requests.post(url, json=data, headers=headers)

        print(response)
        if response.status_code == 200:
            self.set_result(response.json()["fileName"])
        else:
            self.set_exception(Exception("Request failed"))
