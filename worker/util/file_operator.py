import os
from pathlib import Path

class FileOperator:

    @staticmethod
    def write_hash_map_to_file(key_mapping):
        worker_no = os.getenv("workerNo")
        file_path = f"output-{worker_no}.txt"
        output_file_path = Path(file_path)

        with output_file_path.open("w") as bw:
            for key in key_mapping:
                try:
                    bw.write(f"{key},{key_mapping[key]}\n")
                except Exception as e:
                    print(e)

        return file_path
