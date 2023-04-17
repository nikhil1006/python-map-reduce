import requests
from typing import List

class ReduceTracker:

    def __init__(self, worker_port: int, feature: str, intermediate_files: List[str], input_parameter: str = None):
        self.worker_port = worker_port
        self.intermediate_files = intermediate_files
        self.feature = feature
        self.input_parameter = input_parameter

    def run(self):
        url = f"http://127.0.0.1:{self.worker_port}/reduceProcess"

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        data = {
            "feature": self.feature,
            "intermediateFiles": self.intermediate_files
        }

        if self.input_parameter is not None:
            data["misc"] = self.input_parameter

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            return response.text
        else:
            return None
