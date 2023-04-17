import requests

class ReverseWebLinkMapTracker:

    def __init__(self, worker_port: int, start_line: int, end_line: int, file_name: str, feature: str):
        self.worker_port = worker_port
        self.start_line = start_line
        self.end_line = end_line
        self.file_name = file_name
        self.feature = feature

    def run(self):
        url = f"http://127.0.0.1:{self.worker_port}/mapProcess"

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        data = {
            "feature": "ReverseWeblink",
            "fileName": self.file_name,
            "startNo": self.start_line,
            "endNo": self.end_line
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            return response.json()["fileName"]
        else:
            return None

