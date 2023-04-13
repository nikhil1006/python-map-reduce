from pathlib import Path

def get_total_no_of_lines(file_path: str) -> int:
    try:
        with open(file_path, 'r') as file:
            return sum(1 for _ in file)
    except Exception as e:
        print("Exception occurred while extracting file size")
        return -1
