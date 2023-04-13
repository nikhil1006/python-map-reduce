import requests
from typing import Optional

class WordCountMapTracker:

    def __init__(self, worker_port: int, file_name: str, feature: str, start_line: int, end_line: int, input_parameter: Optional[str] = None):
        self.worker_port = worker_port
        self.start_line = start_line
        self.end_line = end_line
        self.file_name = file_name
        self.feature = feature
        self.input_parameter = input_parameter

    def run(self) -> Optional[str]:
        url = f"http://localhost:{self.worker_port}/mapProcess"

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        payload = {
            "feature": self.feature,
            "fileName": self.file_name,
            "startNo": self.start_line,
            "endNo": self.end_line
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response)

        if response.status_code == 200:
            return response.text
        else:
            return None
